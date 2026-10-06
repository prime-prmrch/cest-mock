/**
 * Cambridge English Skills Test (CEST) Simulator
 * Unified Client-Side Engine (v7)
 * 
 * Consolidates procedural assembly, deterministic PRNG (Mulberry32),
 * 52-item objective scoring, CEFR diagnostic evaluation, timer synchronization,
 * and state persistence under Ponytail Ultra architecture (zero build step).
 */

(function (root) {
  'use strict';

  // --- RUNTIME STATE ---
  let currentTestData = null;
  let currentTestId = 1;
  const audioPlays = {};
  let timerInterval = null;

  if (typeof window !== 'undefined') {
    window._examTargetEndTime = window._examTargetEndTime || null;
    window._examIsSubmitted = window._examIsSubmitted || false;
    window.latestReport = window.latestReport || null;
  }

  // =========================================================================
  // 1. DETERMINISTIC PRNG & PROCEDURAL ASSEMBLY
  // =========================================================================

  // 32-bit Murmur/Cyrb string hasher
  function hashString(str) {
    let h1 = 1779033703, h2 = 3144134277, h3 = 1013904242, h4 = 2773480762;
    for (let i = 0, k; i < str.length; i++) {
      k = str.charCodeAt(i);
      h1 = h2 ^ Math.imul(h1 ^ k, 597399067);
      h2 = h3 ^ Math.imul(h2 ^ k, 2869860233);
      h3 = h4 ^ Math.imul(h3 ^ k, 951274213);
      h4 = h1 ^ Math.imul(h4 ^ k, 2716044179);
    }
    h1 = Math.imul(h3 ^ (h1 >>> 18), 597399067);
    h2 = Math.imul(h4 ^ (h2 >>> 22), 2869860233);
    h3 = Math.imul(h1 ^ (h3 >>> 17), 951274213);
    h4 = Math.imul(h2 ^ (h4 >>> 19), 2716044179);
    return ((h1 ^ h2 ^ h3 ^ h4) >>> 0);
  }

  // Fast, high-quality 32-bit PRNG (Mulberry32)
  function createPrng(seedStr) {
    let a = hashString(String(seedStr));
    return function () {
      let t = (a += 0x6D2B79F5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function sampleOne(arr, rng) {
    if (!arr || arr.length === 0) return null;
    const idx = Math.floor(rng() * arr.length);
    return JSON.parse(JSON.stringify(arr[idx]));
  }

  // Deterministic reverse Fisher-Yates array shuffle
  function shuffleArray(arr, rng) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      const temp = a[i];
      a[i] = a[j];
      a[j] = temp;
    }
    return a;
  }

  // Universal Multiple-Choice Option Shuffling & Dynamic Key Remapping
  function shuffleMultipleChoiceQuestion(q, rng) {
    if (!q || !q.options || q.options.length <= 1) return q;
    const originalKey = q.key ? String(q.key).trim().toUpperCase() : "";
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];

    const originalOptions = q.options.map(opt => {
      const clean = opt.label.replace(/^\[[A-Z]\]\s*/i, '').replace(/^[A-Z]\s*-\s*/i, '').trim();
      return {
        origVal: opt.val,
        cleanLabel: clean,
        isCorrect: (opt.val && opt.val.toUpperCase() === originalKey)
      };
    });

    const shuffled = shuffleArray(originalOptions, rng);
    const letterMap = {};
    let newKey = originalKey;

    q.options = shuffled.map((item, idx) => {
      const newLetter = letters[idx];
      letterMap[item.origVal] = newLetter;
      if (item.isCorrect) {
        newKey = newLetter;
      }
      return {
        val: newLetter,
        label: '[' + newLetter + '] ' + item.cleanLabel
      };
    });

    q.key = newKey;
    if (q.trap) {
      q.trap = q.trap.replace(/\[([A-H])\]/g, (match, p1) => {
        return letterMap[p1] ? '[' + letterMap[p1] + ']' : match;
      });
    }
    return q;
  }

  // Reference Options Shuffling (Gapped Sentences/Paragraphs & Multiple Matching)
  function shuffleReferenceOptions(task, rng) {
    if (!task || !task.optionsReference || !task.questions) return task;
    const rawLines = task.optionsReference.split(/<br\s*\/?>/).filter(Boolean);
    const items = [];
    rawLines.forEach(line => {
      const m = line.match(/<strong>\[([A-Z])\]<\/strong>\s*(.*)/i);
      if (m) items.push({ orig: m[1].toUpperCase(), text: m[2].trim() });
    });
    if (items.length <= 1) return task;

    const shuffled = shuffleArray(items, rng);
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
    const letterMap = {};

    shuffled.forEach((item, idx) => {
      const newL = letters[idx];
      letterMap[item.orig] = newL;
      item.newL = newL;
    });

    task.optionsReference = shuffled.map(it => '<strong>[' + it.newL + ']</strong> ' + it.text).join('<br>');

    task.questions.forEach(q => {
      if (q.key && letterMap[q.key.toUpperCase()]) {
        q.key = letterMap[q.key.toUpperCase()];
      }
      q.options = shuffled.map(it => ({
        val: it.newL,
        label: '[' + it.newL + ']'
      }));
      if (q.trap) {
        q.trap = q.trap.replace(/\[([A-H])\]/g, (match, p1) => {
          return letterMap[p1] ? '[' + letterMap[p1] + ']' : match;
        });
      }
    });

    return task;
  }

  /**
   * Procedurally assemble a 52-item exam + 2 writing tasks from bank data
   * Preserves exact 17-step assembly draw sequence.
   */
  function assembleTest(bank, seedInput) {
    const seed = seedInput ? String(seedInput).trim() : String(Math.floor(100000 + Math.random() * 900000));
    const rng = createPrng(seed);

    const test = {
      id: seed,
      seed: seed,
      isProcedural: true,
      title: `Procedural Exam #${seed}`,
      subtitle: `Cambridge General Dynamic Benchmark (Seed ${seed})`,
      durationMinutes: 90,
      audioDir: "",
      reading: [],
      listening: [],
      writing: []
    };

    // =========================================================================
    // READING: 33 QUESTIONS ACROSS TASKS 1 TO 9
    // =========================================================================

    // 1. Reading Task 1: Notice (1 Question, Q1)
    const t1 = sampleOne(bank.reading.task_1_notices, rng);
    if (t1) {
      const q = t1.questions[0];
      q.num = 1;
      q.id = "r_q1";
      q.stem = `1. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      shuffleMultipleChoiceQuestion(q, rng);
      test.reading.push({
        task: 1,
        tag: "Task 1 • Notices & Messages",
        title: t1.title || "Notices & Messages",
        instruction: t1.instruction || "Read the notice and answer the question.",
        passage: t1.passage,
        questions: [q]
      });
    }

    // 2. Reading Task 2: Sentence Cloze (1 Question, Q2)
    const t2 = sampleOne(bank.reading.task_2_sentence_cloze, rng);
    if (t2) {
      const q = t2.questions[0];
      q.num = 2;
      q.id = "r_q2";
      q.stem = `2. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      shuffleMultipleChoiceQuestion(q, rng);
      test.reading.push({
        task: 2,
        tag: "Task 2 • Sentence Gap-Fill",
        title: t2.title || "Sentence Gap-Fill",
        instruction: t2.instruction || "Choose the correct word to complete the sentence.",
        questions: [q]
      });
    }

    // 3. Reading Task 3: Open Cloze (5 Questions, Q3 to Q7)
    const t3 = sampleOne(bank.reading.task_3_open_cloze, rng);
    if (t3) {
      t3.questions.forEach((q, idx) => {
        const qNum = idx + 3;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `Gap ${qNum}`;
      });
      test.reading.push(t3);
    }

    // 4. Reading Task 4: Vocab Cloze (5 Questions, Q8 to Q12)
    const t4 = sampleOne(bank.reading.task_4_vocab_cloze, rng);
    if (t4) {
      t4.questions.forEach((q, idx) => {
        const qNum = idx + 8;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `${qNum}. Choose the best word:`;
        shuffleMultipleChoiceQuestion(q, rng);
      });
      test.reading.push(t4);
    }

    // 5. Reading Task 5: Extended Text (5 Questions, Q13 to Q17)
    const t5 = sampleOne(bank.reading.task_5_extended_text, rng);
    if (t5) {
      t5.questions.forEach((q, idx) => {
        const qNum = idx + 13;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
        shuffleMultipleChoiceQuestion(q, rng);
      });
      test.reading.push(t5);
    }

    // 6. Reading Task 6: Short Article (2 Questions, Q18 to Q19)
    const t6 = sampleOne(bank.reading.task_6_short_article, rng);
    if (t6) {
      t6.questions.forEach((q, idx) => {
        const qNum = idx + 18;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
        shuffleMultipleChoiceQuestion(q, rng);
      });
      test.reading.push(t6);
    }

    // 7. Reading Task 7: Missing Sentences (5 Questions, Q20 to Q24)
    const t7 = sampleOne(bank.reading.task_7_gapped_sentences, rng);
    if (t7) {
      t7.questions.forEach((q, idx) => {
        const qNum = idx + 20;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `Gap ${qNum}`;
      });
      shuffleReferenceOptions(t7, rng);
      test.reading.push(t7);
    }

    // 8. Reading Task 8: Missing Paragraphs (5 Questions, Q25 to Q29)
    const t8 = sampleOne(bank.reading.task_8_gapped_paragraphs, rng);
    if (t8) {
      t8.questions.forEach((q, idx) => {
        const qNum = idx + 25;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `Paragraph Gap ${qNum}`;
      });
      shuffleReferenceOptions(t8, rng);
      test.reading.push(t8);
    }

    // 9. Reading Task 9: Multiple Matching (4 Questions, Q30 to Q33)
    const t9 = sampleOne(bank.reading.task_9_multiple_matching, rng);
    if (t9) {
      t9.questions = shuffleArray(t9.questions, rng);
      t9.questions.forEach((q, idx) => {
        const qNum = idx + 30;
        q.num = qNum;
        q.id = `r_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      });
      test.reading.push(t9);
    }

    // =========================================================================
    // LISTENING: 19 QUESTIONS ACROSS TASKS 1 TO 6
    // =========================================================================

    // Task 1: Short Transactional Dialogue (1 Question, Q1)
    const l1 = sampleOne(bank.listening.task_1_short_dialogue_1, rng);
    if (l1) {
      const q = l1.question;
      q.num = 1;
      q.id = "l_q1";
      q.stem = `1. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      shuffleMultipleChoiceQuestion(q, rng);
      test.listening.push({
        task: 1,
        tag: "Task 1 • Picture Multiple Choice",
        title: l1.title || "Transactional Dialogue",
        instruction: l1.instruction || "Listen to the conversation. (2 plays maximum)",
        audioTrack: l1.audioTrack,
        questions: [q]
      });
    }

    // Task 2: Short Workplace Dialogue (1 Question, Q2)
    const l2 = sampleOne(bank.listening.task_2_short_dialogue_2, rng);
    if (l2) {
      const q = l2.question;
      q.num = 2;
      q.id = "l_q2";
      q.stem = `2. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      shuffleMultipleChoiceQuestion(q, rng);
      test.listening.push({
        task: 2,
        tag: "Task 2 • Short Dialogue Multiple Choice",
        title: l2.title || "Workplace Discussion",
        instruction: l2.instruction || "Listen to the exchange. (2 plays maximum)",
        audioTrack: l2.audioTrack,
        questions: [q]
      });
    }

    // Task 3: Extended Audio Multiple Choice (5 Questions: Q3 to Q7)
    const l3 = sampleOne(bank.listening.task_3_extended_interview, rng);
    if (l3) {
      l3.questions.forEach((q, idx) => {
        const qNum = idx + 3;
        q.num = qNum;
        q.id = `l_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
        shuffleMultipleChoiceQuestion(q, rng);
      });
      test.listening.push(l3);
    }

    // Task 4: Extended Audio Discussion (2 Questions: Q8 to Q9)
    const l4 = sampleOne(bank.listening.task_4_discussion, rng);
    if (l4) {
      l4.questions.forEach((q, idx) => {
        const qNum = idx + 8;
        q.num = qNum;
        q.id = `l_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
        shuffleMultipleChoiceQuestion(q, rng);
      });
      test.listening.push(l4);
    }

    // Task 5: Multiple Matching (5 Questions: Q10 to Q14)
    const l5 = sampleOne(bank.listening.task_5_multiple_matching, rng);
    if (l5) {
      l5.questions.forEach((q, idx) => {
        const qNum = idx + 10;
        q.num = qNum;
        q.id = `l_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      });
      shuffleReferenceOptions(l5, rng);
      test.listening.push(l5);
    }

    // Task 6: Sentence Completion (5 Questions: Q15 to Q19)
    const l6 = sampleOne(bank.listening.task_6_monologue_gaps, rng);
    if (l6) {
      l6.questions.forEach((q, idx) => {
        const qNum = idx + 15;
        q.num = qNum;
        q.id = `l_q${qNum}`;
        q.stem = `${qNum}. ${q.stem.replace(/^\d+\.\s*/, '')}`;
      });
      test.listening.push(l6);
    }

    // =========================================================================
    // WRITING: 2 TASKS (Fix: Assign part: 1 and part: 2 for persistence)
    // =========================================================================
    const w1 = sampleOne(bank.writing.task_1_narrative, rng);
    const w2 = sampleOne(bank.writing.task_2_discursive, rng);
    if (w1) {
      w1.part = 1;
      test.writing.push(w1);
    }
    if (w2) {
      w2.part = 2;
      test.writing.push(w2);
    }

    return test;
  }

  // =========================================================================
  // 2. TEXT NORMALIZATION & UTILITIES
  // =========================================================================

  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // Deduplicated pure string normalizer for open cloze & text gap-fill matching
  function normalizeText(str) {
    return String(str || "")
      .toLowerCase()
      .replace(/[^a-z0-9 ]/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  // =========================================================================
  // 3. OBJECTIVE SCORING & CEFR DIAGNOSTICS (DECOUPLED)
  // =========================================================================

  /**
   * Pure decoupled grading function.
   * If answersDict is provided, evaluates against in-memory dictionary.
   * If omitted, falls back to browser DOM queries.
   */
  function gradeExam(testData, answersDict) {
    const data = testData || currentTestData;
    if (!data) return null;

    let rScore = 0;
    let lScore = 0;
    const breakdown = [];

    function gradeSection(tasks, sectionName, prefix) {
      let score = 0;
      if (!tasks) return score;
      tasks.forEach(task => {
        if (task.questions) {
          task.questions.forEach(q => {
            let userAns = "";
            if (answersDict && answersDict[q.id] !== undefined) {
              userAns = String(answersDict[q.id]);
              if (q.type === "text") userAns = userAns.trim();
            } else if (typeof document !== 'undefined') {
              if (q.type === "mc") {
                const checked = document.querySelector(`input[name="${q.id}"]:checked`);
                userAns = checked ? checked.value : "";
              } else if (q.type === "text") {
                const inp = document.getElementById(q.id);
                userAns = inp ? inp.value.trim() : "";
              } else if (q.type === "select") {
                const sel = document.getElementById(q.id);
                userAns = sel ? sel.value : "";
              }
            }

            let isCorrect = false;
            if (q.type === "text") {
              const normUser = normalizeText(userAns);
              const allowed = [q.key, ...(q.variants || [])].map(normalizeText);
              isCorrect = allowed.includes(normUser);
            } else {
              isCorrect = (String(userAns).trim().toUpperCase() === String(q.key).trim().toUpperCase());
            }

            if (isCorrect) score++;

            breakdown.push({
              section: sectionName,
              id: q.id.replace(prefix, "Q"),
              num: q.num,
              userAns: userAns || "(Blank)",
              correctAns: q.key,
              variants: q.variants || [],
              isCorrect: isCorrect,
              skill: q.skill || (sectionName + " Comprehension"),
              trap: q.trap || "Standard distractor analysis."
            });
          });
        }
      });
      return score;
    }

    rScore = gradeSection(data.reading, "Reading", "r_q");
    lScore = gradeSection(data.listening, "Listening", "l_q");

    const totalScore = rScore + lScore;
    let cefr = "Below A2";
    let cefrTitle = "Needs Foundational Reinforcement";
    let feedback = "Significant reinforcement needed in core syntax, listening decoding, and vocabulary recognition before adaptive testing.";

    if (totalScore >= 46) {
      cefr = "C1";
      cefrTitle = "Advanced Vantage (C1)";
      feedback = "Outstanding performance across macro-cohesion, subtle discourse transitions, and fast monologue comprehension. High readiness for C1 certification.";
    } else if (totalScore >= 38) {
      cefr = "B2";
      cefrTitle = "Independent User (B2 Vantage)";
      feedback = "Solid core communicative competence. Successfully navigates standard workplace and academic scenarios, dropping marks primarily on missing paragraph co-reference and dense monologues.";
    } else if (totalScore >= 28) {
      cefr = "B1";
      cefrTitle = "Threshold Intermediate (B1)";
      feedback = "Competent on straightforward notices and short dialogues. Requires training on open-cloze structural words and multi-speaker inference.";
    } else if (totalScore >= 18) {
      cefr = "A2";
      cefrTitle = "Waystage (A2)";
      feedback = "Basic routine interactions are understood. Needs targeted grammar scaffolding and connected speech decoding drills.";
    }

    let candName = "Student";
    let w1 = "";
    let w2 = "";
    if (answersDict) {
      if (answersDict.candidateName) candName = String(answersDict.candidateName).trim();
      if (answersDict.w_part1 || answersDict.writingPart1) w1 = String(answersDict.w_part1 || answersDict.writingPart1).trim();
      if (answersDict.w_part2 || answersDict.writingPart2) w2 = String(answersDict.w_part2 || answersDict.writingPart2).trim();
    }
    if (typeof document !== 'undefined') {
      if (candName === "Student" && document.getElementById('candidateName')?.value) {
        candName = document.getElementById('candidateName').value.trim() || "Student";
      }
      if (!w1 && document.getElementById('w_part1')?.value) {
        w1 = document.getElementById('w_part1').value.trim();
      }
      if (!w2 && document.getElementById('w_part2')?.value) {
        w2 = document.getElementById('w_part2').value.trim();
      }
    }

    const report = {
      testId: data.id,
      testTitle: data.title,
      candidateName: candName,
      date: new Date().toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }),
      rScore,
      rTotal: 33,
      lScore,
      lTotal: 19,
      totalScore,
      maxScore: 52,
      cefr,
      cefrTitle,
      feedback,
      breakdown,
      writingPart1: w1,
      writingPart2: w2,
      writingTasks: data.writing || []
    };

    if (typeof window !== 'undefined') {
      window.latestReport = report;
    }
    if (typeof document !== 'undefined' && document.getElementById) {
      renderReportUI(report);
    }
    return report;
  }

  function renderReportUI(report) {
    if (typeof document === 'undefined') return;
    const cefrEl = document.getElementById('report_cefr');
    const titleEl = document.getElementById('report_cefr_title');
    const rScoreEl = document.getElementById('report_reading_score');
    const lScoreEl = document.getElementById('report_listening_score');
    const totScoreEl = document.getElementById('report_total_score');
    const feedEl = document.getElementById('report_feedback');

    if (cefrEl) cefrEl.innerText = report.cefr;
    if (titleEl) titleEl.innerText = report.cefrTitle;
    if (rScoreEl) rScoreEl.innerText = `${report.rScore} / ${report.rTotal}`;
    if (lScoreEl) lScoreEl.innerText = `${report.lScore} / ${report.lTotal}`;
    if (totScoreEl) totScoreEl.innerText = `${report.totalScore} / ${report.maxScore}`;
    if (feedEl) feedEl.innerText = report.feedback;

    const reviewList = document.getElementById('review_list');
    if (reviewList) {
      reviewList.innerHTML = "";
      report.breakdown.forEach(item => {
        const div = document.createElement('div');
        div.className = "review-item " + (item.isCorrect ? "correct" : "incorrect");
        div.innerHTML = `
          <div class="review-header">
            <span class="q-number">${item.section} &bull; ${item.id}</span>
            <span class="status-badge ${item.isCorrect ? 'correct' : 'incorrect'}">
              ${item.isCorrect ? 'CORRECT' : 'INCORRECT'}
            </span>
          </div>
          <div class="ans-comparison">
            <strong>Your Answer:</strong> ${escapeHtml(item.userAns)} &nbsp;|&nbsp; 
            <strong>Correct:</strong> <span style="color:var(--success); font-weight:700;">${escapeHtml(item.correctAns)}</span>
            ${item.variants.length > 0 ? `<br><small style="color:var(--text-muted);">Accepted variants: ${item.variants.map(escapeHtml).join(', ')}</small>` : ''}
          </div>
          <button class="rationale-toggle" onclick="CEST.toggleRationale(this)">
            <span>&#9656; View Coach Rationale & Traps</span>
          </button>
          <div class="rationale-content">
            <p><strong>Construct Skill:</strong> ${escapeHtml(item.skill)}</p>
            <p style="margin-top:6px;"><strong>Diagnostic Analysis & Traps:</strong> ${escapeHtml(item.trap)}</p>
          </div>
        `;
        reviewList.appendChild(div);
      });
    }
  }

  function toggleRationale(btn) {
    const content = btn.nextElementSibling;
    if (!content) return;
    const isOpen = content.classList.contains('open');
    if (isOpen) {
      content.classList.remove('open');
      btn.querySelector('span').innerHTML = "&#9656; View Coach Rationale & Traps";
    } else {
      content.classList.add('open');
      btn.querySelector('span').innerHTML = "&#9662; Hide Coach Rationale";
    }
  }

  function generateReportText(report) {
    const rep = report || (typeof window !== 'undefined' ? window.latestReport : null);
    if (!rep) return "No report data available.";

    const incorrectList = rep.breakdown
      .filter(b => !b.isCorrect)
      .map(b => `${b.section} ${b.id}: Selected "${b.userAns}", Expected "${b.correctAns}" [Skill: ${b.skill}]`)
      .join("\n");

    const p1Title = rep.writingTasks[0] ? rep.writingTasks[0].title : "Task 1";
    const p2Title = rep.writingTasks[1] ? rep.writingTasks[1].title : "Task 2";
    const p1Words = rep.writingPart1 ? rep.writingPart1.split(/\s+/).filter(Boolean).length : 0;
    const p2Words = rep.writingPart2 ? rep.writingPart2.split(/\s+/).filter(Boolean).length : 0;

    return `========================================================
CAMBRIDGE ENGLISH SKILLS TEST (GENERAL)
DIAGNOSTIC REPORT FOR COACH
========================================================
Test:            ${rep.testTitle} (ID: ${rep.testId})
Candidate Name:  ${rep.candidateName}
Assessment Date: ${rep.date}

--- OBJECTIVE SCORES ---
Reading:   ${rep.rScore} / ${rep.rTotal}  (${((rep.rScore/rep.rTotal)*100).toFixed(1)}%)
Listening: ${rep.lScore} / ${rep.lTotal}  (${((rep.lScore/rep.lTotal)*100).toFixed(1)}%)
Combined:  ${rep.totalScore} / ${rep.maxScore}  (${((rep.totalScore/rep.maxScore)*100).toFixed(1)}%)
Projected CEFR Level: ${rep.cefr} (${rep.cefrTitle})

Diagnostic Feedback:
${rep.feedback}

--- INCORRECT RESPONSES & DIAGNOSTIC GAPS ---
${incorrectList || "Full Marks! No objective errors recorded."}

========================================================
WRITING SUBMISSION FOR COACH EVALUATION
========================================================

--- PART 1: ${p1Title.toUpperCase()} ---
Word Count: ${p1Words} words
${rep.writingPart1 || "(No submission recorded)"}

--------------------------------------------------------

--- PART 2: ${p2Title.toUpperCase()} ---
Word Count: ${p2Words} words
${rep.writingPart2 || "(No submission recorded)"}

========================================================
`;
  }

  function copyFullCoachReport() {
    const text = generateReportText();
    if (typeof navigator !== 'undefined' && navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        showToast("Full coach report copied to clipboard!");
      }).catch(() => fallbackCopy(text));
    } else {
      fallbackCopy(text);
    }
  }

  function copyWritingOnly() {
    const rep = typeof window !== 'undefined' ? window.latestReport : null;
    const name = (typeof document !== 'undefined' && document.getElementById('candidateName')?.value || "").trim() || "Student";
    const w1 = (typeof document !== 'undefined' && document.getElementById('w_part1')?.value || "").trim();
    const w2 = (typeof document !== 'undefined' && document.getElementById('w_part2')?.value || "").trim();
    const p1Title = (rep && rep.writingTasks[0]) ? rep.writingTasks[0].title : "Task 1";
    const p2Title = (rep && rep.writingTasks[1]) ? rep.writingTasks[1].title : "Task 2";

    const text = `STUDENT WRITING SUBMISSION
Candidate: ${name}
Date: ${new Date().toLocaleDateString()}

--- PART 1: ${p1Title} ---
Word Count: ${w1.split(/\s+/).filter(Boolean).length} words
${w1 || "(No text)"}

--------------------------------------------------------

--- PART 2: ${p2Title} ---
Word Count: ${w2.split(/\s+/).filter(Boolean).length} words
${w2 || "(No text)"}
`;

    if (typeof navigator !== 'undefined' && navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        showToast("Writing essays copied to clipboard!");
      }).catch(() => fallbackCopy(text));
    } else {
      fallbackCopy(text);
    }
  }

  function fallbackCopy(text) {
    if (typeof document === 'undefined') return;
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    try {
      document.execCommand('copy');
      showToast("Copied to clipboard!");
    } catch (err) {
      if (typeof alert !== 'undefined') alert("Please copy manually from the report section.");
    }
    document.body.removeChild(ta);
  }

  function downloadReportTxt() {
    const text = generateReportText();
    const rep = typeof window !== 'undefined' ? window.latestReport : null;
    const safeName = (rep?.candidateName || "Candidate").replace(/[^a-zA-Z0-9_-]/g, "_");
    const testNum = rep?.testId || 1;
    const filename = `CEST_Mock_Test_${testNum}_Report_${safeName}.txt`;

    const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    showToast("Report downloaded as text file!");
  }

  // =========================================================================
  // 4. INTERACTIVE TEST RUNNER & TIMERS
  // =========================================================================

  async function initEngine() {
    if (typeof window === 'undefined') return;
    const urlParams = new URLSearchParams(window.location.search);
    const seedParam = urlParams.get('seed');
    const idParam = urlParams.get('id');

    const isArchival = Boolean(idParam && [1, 2, 3].includes(parseInt(idParam)));
    let activeSeed;

    if (isArchival) {
      currentTestId = parseInt(idParam);
      updatePortalNav(currentTestId);
    } else {
      if (seedParam && seedParam.trim()) {
        activeSeed = seedParam.trim();
      } else {
        const savedActiveSeed = localStorage.getItem('cest_active_seed');
        if (savedActiveSeed && savedActiveSeed.trim()) {
          activeSeed = savedActiveSeed.trim();
        } else {
          activeSeed = String(Math.floor(100000 + Math.random() * 900000));
        }
      }

      currentTestId = activeSeed;
      try {
        localStorage.setItem('cest_active_seed', activeSeed);
      } catch (e) {
        console.warn("Storage write error:", e);
      }

      if (!window.location.search.includes(`seed=${encodeURIComponent(activeSeed)}`)) {
        const newUrl = `${window.location.pathname}?seed=${encodeURIComponent(activeSeed)}`;
        window.history.replaceState({ seed: activeSeed }, '', newUrl);
      }

      updatePortalNavProcedural(activeSeed);
    }

    try {
      if (!isArchival) {
        const res = await fetch('data/bank.json?v=7');
        if (!res.ok) throw new Error(`HTTP ${res.status}: Failed to load bank.json.`);
        const bank = await res.json();
        currentTestData = assembleTest(bank, activeSeed);
      } else {
        const res = await fetch(`data/test_${currentTestId}.json?v=7`);
        if (!res.ok) throw new Error(`HTTP ${res.status}: Failed to load test data.`);
        currentTestData = await res.json();
      }

      renderExam(currentTestData);
      loadSavedState();
      startTimer(currentTestData.durationMinutes || 90);
    } catch (err) {
      console.error("Test initialization error:", err);
      const container = document.querySelector('.container');
      if (container) {
        container.innerHTML = `
          <div class="task-card" style="text-align:center; padding:40px 20px;">
            <h2 style="color:var(--danger); margin-bottom:12px;">Failed to Load Test Data</h2>
            <p style="color:var(--text-muted); margin-bottom:20px;">Could not retrieve test content. Please verify data files and reload.</p>
            <a href="index.html" class="btn btn-primary" style="display:inline-block;">Return to Portal Hub</a>
          </div>
        `;
      }
    }
  }

  function updatePortalNavProcedural(seed) {
    const portalBar = document.querySelector('.portal-bar');
    if (!portalBar) return;
    portalBar.innerHTML = `
      <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
        <a href="index.html" style="color:var(--secondary); text-decoration:none; padding:3px 8px; border-radius:4px; font-weight:700;">&#127968; Hub</a>
        <span style="background:#e8f1fa; color:var(--primary); padding:2px 8px; border-radius:12px; font-size:11px; font-weight:700;">🎲 Seed #${escapeHtml(seed)}</span>
      </div>
      <div style="display:flex; align-items:center; gap:8px;">
        <button type="button" onclick="CEST.copySeedLink('${escapeHtml(seed)}')" style="background:var(--secondary); color:white; border:none; border-radius:4px; padding:4px 10px; font-size:11px; font-weight:700; cursor:pointer;">🔗 Share Seed</button>
        <button type="button" onclick="CEST.startNewExam()" style="background:#f1f5f9; color:var(--text); border:none; border-radius:4px; padding:4px 10px; font-size:11px; font-weight:700; cursor:pointer;">🔄 New Random</button>
      </div>
    `;
  }

  function startNewExam(force = false) {
    if (!force) {
      const proceed = confirm("Generate a brand new random exam? This will close your current session.");
      if (!proceed) return;
    }
    const freshSeed = String(Math.floor(100000 + Math.random() * 900000));
    localStorage.removeItem('cest_active_seed');
    window.location.href = `test.html?seed=${freshSeed}`;
  }

  function copySeedLink(seed) {
    const shareUrl = `${window.location.origin}${window.location.pathname}?seed=${encodeURIComponent(seed)}`;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(shareUrl).then(() => {
        showToast(`Copied Exam Link (Seed #${seed}) to clipboard!`);
      }).catch(() => fallbackCopy(shareUrl));
    } else {
      fallbackCopy(shareUrl);
    }
  }

  function updatePortalNav(testId) {
    const portalLinks = document.querySelectorAll('.portal-bar a');
    portalLinks.forEach(link => {
      const href = link.getAttribute('href') || "";
      if (href.includes(`id=${testId}`) || (testId === 1 && href.endsWith('test.html'))) {
        link.style.background = "var(--primary)";
        link.style.color = "white";
      } else if (href.includes('index.html')) {
        link.style.background = "transparent";
        link.style.color = "var(--secondary)";
      } else {
        link.style.background = "transparent";
        link.style.color = "var(--secondary)";
      }
    });
  }

  function renderExam(data) {
    document.title = `${data.title} | Cambridge Mock Simulator`;

    const logoBadge = document.querySelector('.logo-badge');
    if (logoBadge) {
      logoBadge.innerHTML = `
        <span class="badge-icon">TEST ${data.id}</span>
        <span class="badge-title">${escapeHtml(data.title.split(':')[0])}</span>
      `;
    }

    const rContainer = document.getElementById('section-reading');
    if (rContainer && data.reading) {
      rContainer.innerHTML = data.reading.map(task => renderReadingTask(task)).join('');
    }

    const lContainer = document.getElementById('section-listening');
    if (lContainer && data.listening) {
      lContainer.innerHTML = data.listening.map(task => renderListeningTask(task, data.audioDir)).join('');
    }

    const wContainer = document.getElementById('section-writing');
    if (wContainer && data.writing) {
      wContainer.innerHTML = data.writing.map(task => renderWritingTask(task)).join('');
    }

    attachInputListeners();
  }

  function renderReadingTask(task) {
    let innerBody = "";
    if (task.passage) {
      innerBody += `<div class="passage-box">${task.passage}</div>`;
    }
    if (task.optionsReference) {
      innerBody += `<div style="background:#e8f1fa; padding:12px; border-radius:8px; margin-bottom:14px; font-size:13px; line-height:1.5;">${task.optionsReference}</div>`;
    }
    if (task.questions) {
      innerBody += task.questions.map(q => renderQuestion(q)).join('');
    }
    return `
      <div class="task-card" id="task_r_${task.task}">
        <div class="task-header">
          <span class="task-tag">${escapeHtml(task.tag)}</span>
          <h3 class="task-title">${escapeHtml(task.title)}</h3>
          <div class="task-instructions">${escapeHtml(task.instruction)}</div>
        </div>
        ${innerBody}
      </div>
    `;
  }

  function renderListeningTask(task, audioDir) {
    const audioId = `audio_l_t${task.task}`;
    const btnId = `btn_l_t${task.task}`;
    const badgeId = `badge_l_t${task.task}`;
    const progId = `prog_l_t${task.task}`;
    const timeId = `time_l_t${task.task}`;

    let innerBody = `
      <div class="audio-player-card">
        <div class="audio-player-top">
          <span class="audio-title">${escapeHtml(task.title)} (Audio Track)</span>
          <span class="audio-counter" id="${badgeId}">Plays left: 2</span>
        </div>
        <div class="audio-controls">
          <button type="button" class="play-btn" id="${btnId}" onclick="CEST.playAudio('${audioId}', '${btnId}', '${badgeId}', '${progId}', '${timeId}')">&#9658;</button>
          <div class="audio-progress-bar">
            <div class="audio-progress-fill" id="${progId}"></div>
          </div>
          <span class="audio-time-label" id="${timeId}">0:00</span>
        </div>
        <audio id="${audioId}" preload="none" src="${(task.audioTrack.startsWith('audio/') || task.audioTrack.startsWith('mock_test_')) ? task.audioTrack : (audioDir || '') + task.audioTrack}"></audio>
      </div>
    `;

    if (task.optionsReference) {
      innerBody += `<div style="background:#e8f1fa; padding:12px; border-radius:8px; margin-bottom:14px; font-size:13px; line-height:1.5;">${task.optionsReference}</div>`;
    }
    if (task.questions) {
      innerBody += task.questions.map(q => renderQuestion(q)).join('');
    }
    return `
      <div class="task-card" id="task_l_${task.task}">
        <div class="task-header">
          <span class="task-tag">${escapeHtml(task.tag)}</span>
          <h3 class="task-title">${escapeHtml(task.title)}</h3>
          <div class="task-instructions">${escapeHtml(task.instruction)}</div>
        </div>
        ${innerBody}
      </div>
    `;
  }

  function renderQuestion(q) {
    if (q.type === "mc") {
      const opts = (q.options || []).map(opt => `
        <label class="option-card" onclick="CEST.selectOption(this)">
          <input type="radio" name="${q.id}" value="${opt.val}">
          <span class="option-label">${escapeHtml(opt.label)}</span>
        </label>
      `).join('');

      return `
        <div class="question-block" id="qb_${q.id}">
          ${q.stem ? `<div class="question-stem">${escapeHtml(q.stem)}</div>` : ''}
          <div class="options-grid">
            ${opts}
          </div>
        </div>
      `;
    } else if (q.type === "text") {
      return `
        <div class="question-block" id="qb_${q.id}">
          ${q.stem ? `<div class="question-stem">${escapeHtml(q.stem)}</div>` : ''}
          <div class="gap-input-wrap">
            <span>(${q.num})</span>
            <input type="text" class="gap-text-input" id="${q.id}" placeholder="Type word..." autocomplete="off" spellcheck="false">
          </div>
        </div>
      `;
    } else if (q.type === "select") {
      const opts = (q.options || []).map(opt => `
        <option value="${opt.val}">${escapeHtml(opt.label)}</option>
      `).join('');

      return `
        <div class="question-block" id="qb_${q.id}">
          ${q.stem ? `<div class="question-stem">${escapeHtml(q.stem)}</div>` : ''}
          <div class="gap-input-wrap">
            <span>${q.num}.</span>
            <select class="select-input" id="${q.id}">
              <option value="">-- Choose ${q.num} --</option>
              ${opts}
            </select>
          </div>
        </div>
      `;
    }
    return "";
  }

  function renderWritingTask(task) {
    const textId = `w_part${task.part}`;
    const badgeId = `badge_w_part${task.part}`;
    const minWords = task.minWords || (task.part === 2 ? 220 : 150);

    return `
      <div class="task-card" id="task_w_${task.part}">
        <div class="task-header">
          <span class="task-tag">${escapeHtml(task.tag)}</span>
          <h3 class="task-title">${escapeHtml(task.title)}</h3>
          <div class="task-instructions">${escapeHtml(task.instruction)}</div>
        </div>
        <div class="passage-box">
          ${task.prompt}
        </div>
        <textarea class="essay-textarea" id="${textId}" placeholder="Compose your response here..." oninput="CEST.handleWritingInput('${textId}', '${badgeId}', ${minWords})"></textarea>
        <div class="writing-footer">
          <span class="word-count-badge" id="${badgeId}">0 words (Min: ${minWords})</span>
          <button type="button" class="btn btn-secondary" style="padding:6px 12px; font-size:13px;" onclick="CEST.copySingleWriting('${textId}', '${escapeHtml(task.title)}')">Copy Draft</button>
        </div>
      </div>
    `;
  }

  function switchSection(secId) {
    if (typeof document === 'undefined') return;
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.section-view').forEach(view => view.classList.remove('active'));

    const tabIndexMap = { reading: 0, listening: 1, writing: 2, results: 3 };
    const btns = document.querySelectorAll('.tab-bar .tab-btn');
    if (btns[tabIndexMap[secId]]) {
      btns[tabIndexMap[secId]].classList.add('active');
    }

    const activeView = document.getElementById(`section-${secId}`);
    if (activeView) {
      activeView.classList.add('active');
      if (typeof window !== 'undefined' && window.scrollTo) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }
  }

  function selectOption(cardEl) {
    const radio = cardEl.querySelector('input[type="radio"]');
    if (!radio) return;

    const groupName = radio.name;
    document.querySelectorAll(`input[name="${groupName}"]`).forEach(r => {
      r.checked = false;
      const parent = r.closest('.option-card');
      if (parent) parent.classList.remove('selected');
    });

    radio.checked = true;
    cardEl.classList.add('selected');
    saveState();
    updateProgressBadge();
  }

  function playAudio(audioId, btnId, badgeId, progId, timeId) {
    const audio = document.getElementById(audioId);
    const btn = document.getElementById(btnId);
    const badge = document.getElementById(badgeId);
    const prog = document.getElementById(progId);
    const timeLbl = document.getElementById(timeId);

    if (!audio || !btn || !badge) return;

    if (!audioPlays[audioId]) {
      audioPlays[audioId] = { count: 0, max: 2, isPlaying: false };
    }
    const state = audioPlays[audioId];

    if (state.isPlaying) {
      audio.pause();
      state.isPlaying = false;
      btn.innerHTML = "&#9658;";
      return;
    }

    if (state.count >= state.max) {
      showToast("Maximum 2 plays reached for this track!");
      return;
    }

    if (audio.currentTime === 0 || audio.ended) {
      state.count++;
      saveState();
      const remaining = state.max - state.count;
      badge.innerText = "Plays left: " + remaining;
      if (remaining === 0) badge.classList.add('depleted');
    }

    document.querySelectorAll('audio').forEach(a => {
      if (a !== audio) {
        a.pause();
        a.currentTime = 0;
      }
    });
    document.querySelectorAll('.play-btn').forEach(b => {
      if (b !== btn) b.innerHTML = "&#9658;";
    });

    audio.play().then(() => {
      state.isPlaying = true;
      btn.innerHTML = "&#10074;&#10074;";
    }).catch(err => {
      console.warn("Playback prevented:", err);
      showToast("Tap again to play audio.");
    });

    audio.ontimeupdate = () => {
      if (audio.duration) {
        const pct = (audio.currentTime / audio.duration) * 100;
        if (prog) prog.style.width = pct + "%";
        const m = Math.floor(audio.currentTime / 60);
        const s = Math.floor(audio.currentTime % 60);
        if (timeLbl) timeLbl.innerText = `${m}:${s < 10 ? '0' : ''}${s}`;
      }
    };

    audio.onended = () => {
      state.isPlaying = false;
      btn.innerHTML = "&#9658;";
      if (prog) prog.style.width = "0%";
      audio.currentTime = 0;
      if (state.count >= state.max) {
        btn.disabled = true;
        btn.style.opacity = "0.5";
        badge.innerText = "No plays left";
        badge.classList.add('depleted');
      }
      saveState();
    };
  }

  function handleWritingInput(textareaId, badgeId, minWords) {
    const ta = document.getElementById(textareaId);
    const badge = document.getElementById(badgeId);
    if (!ta || !badge) return;

    const words = ta.value.trim().split(/\s+/).filter(Boolean).length;
    badge.innerText = `${words} words (Min: ${minWords})`;

    if (words >= minWords) {
      badge.classList.add('valid');
    } else {
      badge.classList.remove('valid');
    }

    saveState();
  }

  function copySingleWriting(textId, taskTitle) {
    const text = (document.getElementById(textId)?.value || "").trim();
    if (!text) {
      showToast("Writing area is currently empty.");
      return;
    }
    const payload = `=== ${taskTitle.toUpperCase()} ===\n${text}`;
    navigator.clipboard.writeText(payload).then(() => {
      showToast("Draft copied to clipboard!");
    }).catch(() => fallbackCopy(payload));
  }

  function startTimer(durationMinutes) {
    const timerBadge = document.getElementById('examTimer');
    if (!timerBadge) return;

    if (timerInterval) clearInterval(timerInterval);

    if (window._examIsSubmitted) {
      timerBadge.innerText = "Submitted";
      timerBadge.style.color = "var(--success)";
      timerBadge.style.borderColor = "var(--success)";
      return;
    }

    if (!window._examTargetEndTime) {
      window._examTargetEndTime = Date.now() + (durationMinutes * 60 * 1000);
      saveState();
    }

    const updateDisplay = () => {
      if (window._examIsSubmitted) {
        clearInterval(timerInterval);
        timerBadge.innerText = "Submitted";
        return;
      }

      const now = Date.now();
      const remainingMs = Math.max(0, window._examTargetEndTime - now);
      const totalSeconds = Math.floor(remainingMs / 1000);

      if (totalSeconds <= 0) {
        clearInterval(timerInterval);
        timerBadge.innerText = "00:00";
        timerBadge.style.color = "var(--danger)";
        timerBadge.style.borderColor = "var(--danger)";
        showToast("Time has expired! Submitting test automatically...");
        submitExam(true);
        return;
      }

      const m = Math.floor(totalSeconds / 60);
      const s = Math.floor(totalSeconds % 60);
      timerBadge.innerText = `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;

      if (totalSeconds <= 600) {
        timerBadge.style.color = "var(--danger)";
        timerBadge.style.borderColor = "var(--danger)";
      } else {
        timerBadge.style.color = "";
        timerBadge.style.borderColor = "";
      }
    };

    updateDisplay();
    timerInterval = setInterval(updateDisplay, 1000);
  }

  function showToast(msg) {
    if (typeof document === 'undefined') return;
    const t = document.getElementById('toast');
    if (!t) return;
    t.innerText = msg;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 2600);
  }

  // =========================================================================
  // 5. LOCAL STORAGE SESSION STATE MANAGEMENT
  // =========================================================================

  function saveState() {
    if (!currentTestData) return;
    const state = {
      testId: currentTestId,
      candidateName: (typeof document !== 'undefined' && document.getElementById('candidateName')?.value) || "",
      targetEndTime: (typeof window !== 'undefined' ? window._examTargetEndTime : null) || null,
      isSubmitted: (typeof window !== 'undefined' ? window._examIsSubmitted : false) || false,
      audioPlays: {},
      radios: {},
      texts: {},
      selects: {},
      writing: {
        part1: (typeof document !== 'undefined' && document.getElementById('w_part1')?.value) || "",
        part2: (typeof document !== 'undefined' && document.getElementById('w_part2')?.value) || ""
      },
      updatedAt: Date.now()
    };

    for (let aid in audioPlays) {
      state.audioPlays[aid] = {
        count: audioPlays[aid].count,
        max: audioPlays[aid].max || 2
      };
    }

    if (typeof document !== 'undefined') {
      document.querySelectorAll('input[type="radio"]:checked').forEach(r => {
        state.radios[r.name] = r.value;
      });

      document.querySelectorAll('.gap-text-input').forEach(inp => {
        if (inp.value) state.texts[inp.id] = inp.value;
      });

      document.querySelectorAll('.select-input').forEach(sel => {
        if (sel.value) state.selects[sel.id] = sel.value;
      });
    }

    try {
      if (typeof localStorage !== 'undefined') {
        localStorage.setItem(`cest_mock_${currentTestId}_state`, JSON.stringify(state));
      }
    } catch (e) {
      console.warn("Storage quota exceeded", e);
    }
  }

  function loadSavedState() {
    try {
      if (typeof localStorage === 'undefined') return;
      const raw = localStorage.getItem(`cest_mock_${currentTestId}_state`);
      if (!raw) return;
      const state = JSON.parse(raw);

      if (state.candidateName && typeof document !== 'undefined' && document.getElementById('candidateName')) {
        document.getElementById('candidateName').value = state.candidateName;
      }

      if (state.targetEndTime && typeof window !== 'undefined') {
        window._examTargetEndTime = state.targetEndTime;
      }

      if (state.isSubmitted && typeof window !== 'undefined') {
        window._examIsSubmitted = true;
      }

      if (state.audioPlays && typeof document !== 'undefined') {
        for (let aid in state.audioPlays) {
          const item = state.audioPlays[aid];
          audioPlays[aid] = { count: item.count || 0, max: item.max || 2, isPlaying: false };
          const remaining = Math.max(0, (item.max || 2) - (item.count || 0));
          const badge = document.getElementById(aid.replace('audio_', 'badge_'));
          const btn = document.getElementById(aid.replace('audio_', 'btn_'));
          if (badge) {
            badge.innerText = remaining === 0 ? "No plays left" : `Plays left: ${remaining}`;
            if (remaining === 0) badge.classList.add('depleted');
          }
          if (btn && remaining === 0) {
            btn.disabled = true;
            btn.style.opacity = "0.5";
          }
        }
      }

      if (state.radios && typeof document !== 'undefined') {
        for (let qid in state.radios) {
          const val = state.radios[qid];
          const r = document.querySelector(`input[name="${qid}"][value="${val}"]`);
          if (r) {
            r.checked = true;
            const parent = r.closest('.option-card');
            if (parent) parent.classList.add('selected');
          }
        }
      }

      if (state.texts && typeof document !== 'undefined') {
        for (let qid in state.texts) {
          const inp = document.getElementById(qid);
          if (inp) inp.value = state.texts[qid];
        }
      }

      if (state.selects && typeof document !== 'undefined') {
        for (let qid in state.selects) {
          const sel = document.getElementById(qid);
          if (sel) sel.value = state.selects[qid];
        }
      }

      if (state.writing && typeof document !== 'undefined') {
        if (state.writing.part1 && document.getElementById('w_part1')) {
          document.getElementById('w_part1').value = state.writing.part1;
          handleWritingInput('w_part1', 'badge_w_part1', 150);
        }
        if (state.writing.part2 && document.getElementById('w_part2')) {
          document.getElementById('w_part2').value = state.writing.part2;
          handleWritingInput('w_part2', 'badge_w_part2', 220);
        }
      }

      updateProgressBadge();

      if (state.isSubmitted) {
        gradeExam(currentTestData);
        switchSection('results');
      }
    } catch (err) {
      console.warn("Failed to load saved test state:", err);
    }
  }

  let saveDebounceTimer = null;
  function debouncedSaveState() {
    if (saveDebounceTimer) clearTimeout(saveDebounceTimer);
    saveDebounceTimer = setTimeout(() => {
      saveState();
      updateProgressBadge();
    }, 200);
  }

  function attachInputListeners() {
    if (typeof document === 'undefined') return;
    document.querySelectorAll('.gap-text-input').forEach(inp => {
      inp.addEventListener('input', debouncedSaveState);
    });

    document.querySelectorAll('.select-input').forEach(sel => {
      sel.addEventListener('change', () => {
        saveState();
        updateProgressBadge();
      });
    });

    const nameInput = document.getElementById('candidateName');
    if (nameInput) {
      nameInput.addEventListener('input', debouncedSaveState);
    }
  }

  function countAnswered() {
    let answered = 0;
    if (typeof document === 'undefined') return answered;
    const checkedRadios = document.querySelectorAll('input[type="radio"]:checked');
    answered += checkedRadios.length;
    document.querySelectorAll('.gap-text-input').forEach(inp => {
      if (inp.value && inp.value.trim().length > 0) answered++;
    });
    document.querySelectorAll('.select-input').forEach(sel => {
      if (sel.value && sel.value.length > 0) answered++;
    });
    return answered;
  }

  function updateProgressBadge() {
    if (typeof document === 'undefined') return;
    const answered = countAnswered();
    const progEl = document.getElementById('answeredProgress');
    if (progEl) {
      progEl.innerText = `${answered} / 52 answered`;
    }
  }

  function submitExam(force = false) {
    if (!currentTestData) return;

    const answered = countAnswered();
    if (!force && answered < 52) {
      const proceed = confirm(`You have completed ${answered} of 52 objective questions. Would you like to submit now and view your diagnostic evaluation?`);
      if (!proceed) return;
    }

    if (typeof window !== 'undefined') window._examIsSubmitted = true;
    saveState();
    if (timerInterval) clearInterval(timerInterval);
    const timerBadge = document.getElementById('examTimer');
    if (timerBadge) {
      timerBadge.innerText = "Submitted";
      timerBadge.style.color = "var(--success)";
      timerBadge.style.borderColor = "var(--success)";
    }

    gradeExam(currentTestData);
    switchSection('results');
    showToast("Exam successfully scored! Diagnostic report generated.");
  }

  function resetExam() {
    const proceed = confirm("Are you sure you want to reset all answers and retake this test?");
    if (!proceed) return;

    localStorage.removeItem(`cest_mock_${currentTestId}_state`);
    window.location.reload();
  }

  // =========================================================================
  // 6. INITIALIZATION & EXPORTS
  // =========================================================================

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
      if (document.getElementById('section-reading')) {
        initEngine();
      }
    });
  }

  const CEST = {
    hashString,
    createPrng,
    shuffleArray,
    shuffleMultipleChoiceQuestion,
    shuffleReferenceOptions,
    assembleTest,
    normalizeText,
    gradeExam,
    renderReportUI,
    toggleRationale,
    generateReportText,
    copyFullCoachReport,
    copyWritingOnly,
    fallbackCopy,
    downloadReportTxt,
    initEngine,
    updatePortalNavProcedural,
    updatePortalNav,
    startNewExam,
    copySeedLink,
    renderExam,
    renderReadingTask,
    renderListeningTask,
    renderQuestion,
    renderWritingTask,
    switchSection,
    selectOption,
    playAudio,
    handleWritingInput,
    copySingleWriting,
    startTimer,
    showToast,
    saveState,
    loadSavedState,
    countAnswered,
    updateProgressBadge,
    submitExam,
    resetExam,
    escapeHtml
  };

  // Browser global exposure & backward compatibility
  if (typeof window !== 'undefined') {
    window.CEST = CEST;
    window.CESTProcedural = CEST;
    window.gradeExam = gradeExam;
    window.generateReportText = generateReportText;
    window.saveState = saveState;
    window.loadSavedState = loadSavedState;
    window.escapeHtml = escapeHtml;
    window.switchSection = switchSection;
    window.selectOption = selectOption;
    window.playAudio = playAudio;
    window.handleWritingInput = handleWritingInput;
    window.copySingleWriting = copySingleWriting;
    window.copyFullCoachReport = copyFullCoachReport;
    window.copyWritingOnly = copyWritingOnly;
    window.downloadReportTxt = downloadReportTxt;
    window.submitExam = submitExam;
    window.resetExam = resetExam;
    window.toggleRationale = toggleRationale;
    window.startNewExam = startNewExam;
    window.copySeedLink = copySeedLink;
  }

  // Node.js runtime / global scope bindings
  if (typeof global !== 'undefined') {
    global.CEST = CEST;
    global.CESTProcedural = CEST;
    global.gradeExam = gradeExam;
    global.generateReportText = generateReportText;
    global.saveState = saveState;
    global.loadSavedState = loadSavedState;
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = CEST;
  }

})(typeof window !== 'undefined' ? window : (typeof global !== 'undefined' ? global : this));
