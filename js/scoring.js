/**
 * Cambridge English Skills Test (General)
 * Scoring & Diagnostic Evaluation Engine
 */

window.latestReport = null;

function gradeExam(testData) {
  let rScore = 0;
  let lScore = 0;
  const breakdown = [];

  // Grade Reading
  if (testData.reading) {
    testData.reading.forEach(task => {
      if (task.questions) {
        task.questions.forEach(q => {
          let userAns = "";
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

          let isCorrect = false;
          if (q.type === "text") {
            const normUser = userAns.toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " ");
            const allowed = [q.key, ...(q.variants || [])].map(v => v.toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " "));
            isCorrect = allowed.includes(normUser);
          } else {
            isCorrect = (userAns.toUpperCase() === q.key.toUpperCase());
          }

          if (isCorrect) rScore++;

          breakdown.push({
            section: "Reading",
            id: q.id.replace("r_q", "Q"),
            num: q.num,
            userAns: userAns || "(Blank)",
            correctAns: q.key,
            variants: q.variants || [],
            isCorrect: isCorrect,
            skill: q.skill || "Reading Comprehension",
            trap: q.trap || "Standard distractor analysis."
          });
        });
      }
    });
  }

  // Grade Listening
  if (testData.listening) {
    testData.listening.forEach(task => {
      if (task.questions) {
        task.questions.forEach(q => {
          let userAns = "";
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

          let isCorrect = false;
          if (q.type === "text") {
            const normUser = userAns.toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " ");
            const allowed = [q.key, ...(q.variants || [])].map(v => v.toLowerCase().replace(/[^a-z0-9 ]/g, "").replace(/\s+/g, " "));
            isCorrect = allowed.includes(normUser);
          } else {
            isCorrect = (userAns.toUpperCase() === q.key.toUpperCase());
          }

          if (isCorrect) lScore++;

          breakdown.push({
            section: "Listening",
            id: q.id.replace("l_q", "Q"),
            num: q.num,
            userAns: userAns || "(Blank)",
            correctAns: q.key,
            variants: q.variants || [],
            isCorrect: isCorrect,
            skill: q.skill || "Listening Comprehension",
            trap: q.trap || "Standard distractor analysis."
          });
        });
      }
    });
  }

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

  const candName = (document.getElementById('candidateName')?.value || "").trim() || "Student";
  const w1 = (document.getElementById('w_part1')?.value || "").trim();
  const w2 = (document.getElementById('w_part2')?.value || "").trim();

  const report = {
    testId: testData.id,
    testTitle: testData.title,
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
    writingTasks: testData.writing || []
  };

  window.latestReport = report;
  renderReportUI(report);
  return report;
}

function renderReportUI(report) {
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
        <button class="rationale-toggle" onclick="toggleRationale(this)">
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
  const rep = report || window.latestReport;
  if (!rep) return "No report data available.";

  const incorrectList = rep.breakdown
    .filter(b => !b.isCorrect)
    .map(b => `${b.section} ${b.id}: Selected "${b.userAns}", Expected "${b.correctAns}" [Skill: ${b.skill}]`)
    .join("\n");

  const p1Title = rep.writingTasks[0] ? rep.writingTasks[0].title : "Task 1";
  const p2Title = rep.writingTasks[1] ? rep.writingTasks[1].title : "Task 2";
  const p1Words = rep.writingPart1.split(/\s+/).filter(Boolean).length;
  const p2Words = rep.writingPart2.split(/\s+/).filter(Boolean).length;

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
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(() => {
      showToast("Full coach report copied to clipboard!");
    }).catch(() => fallbackCopy(text));
  } else {
    fallbackCopy(text);
  }
}

function copyWritingOnly() {
  const rep = window.latestReport;
  const name = (document.getElementById('candidateName')?.value || "").trim() || "Student";
  const w1 = (document.getElementById('w_part1')?.value || "").trim();
  const w2 = (document.getElementById('w_part2')?.value || "").trim();
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

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(() => {
      showToast("Writing essays copied to clipboard!");
    }).catch(() => fallbackCopy(text));
  } else {
    fallbackCopy(text);
  }
}

function fallbackCopy(text) {
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
    alert("Please copy manually from the report section.");
  }
  document.body.removeChild(ta);
}

function downloadReportTxt() {
  const text = generateReportText();
  const rep = window.latestReport;
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

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
