/**
 * Cambridge English Skills Test Simulator
 * Procedural Test Assembler & Deterministic Seed PRNG (Mulberry32)
 * Strictly Calibrated to the 52-Question Objective Specification:
 * - Reading: 33 Questions across Tasks 1–9
 * - Listening: 19 Questions across Tasks 1–6
 * - Writing: 2 Tasks
 */

(function (window) {
  'use strict';

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

  // Fast, high-quality 32-bit PRNG
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

  /**
   * Procedurally assemble a 52-item exam + 2 writing tasks from bank data
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
      test.reading.push(t8);
    }

    // 9. Reading Task 9: Multiple Matching (4 Questions, Q30 to Q33)
    const t9 = sampleOne(bank.reading.task_9_multiple_matching, rng);
    if (t9) {
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
    // WRITING: 2 TASKS
    // =========================================================================
    const w1 = sampleOne(bank.writing.task_1_narrative, rng);
    const w2 = sampleOne(bank.writing.task_2_discursive, rng);
    if (w1) test.writing.push(w1);
    if (w2) test.writing.push(w2);

    return test;
  }

  window.CESTProcedural = {
    hashString,
    createPrng,
    assembleTest
  };

})(window);
