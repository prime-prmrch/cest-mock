# Cambridge English Skills Test (CEST) — Procedural Diagnostic Simulator

[![Live Portal](https://img.shields.io/badge/Live%20Portal-GitHub%20Pages-0077b6?style=flat-square)](https://prime-prmrch.github.io/cest-mock/)
[![Engine](https://img.shields.io/badge/Engine-Procedural%20PRNG-blueviolet?style=flat-square)](#-the-solution-institutional-grade-procedural-simulation)
[![PWA](https://img.shields.io/badge/PWA-Offline%20Ready-success?style=flat-square)](#-offline-resilience--mobile-pwa)
[![Audio](https://img.shields.io/badge/Audio-30%20Neural%20Tracks-purple?style=flat-square)](#-authentic-neural-listening-bank-30-tracks)
[![CEFR Level](https://img.shields.io/badge/CEFR-A2%20to%20C1%20Calibrated-orange?style=flat-square)](#-cefr-diagnostic-banding-matrix)

An institutional-grade, zero-marginal-cost diagnostic simulator designed to prepare candidates for the **Cambridge English Skills Test (General)** and high-stakes university admissions benchmarks (such as **IUP Universitas Airlangga**).

**Interactive Web Application**: [https://prime-prmrch.github.io/cest-mock/](https://prime-prmrch.github.io/cest-mock/)  
**Lead Curriculum Architect**: Febrian Dhani Hartawan (*Department of English Language and Literature, Universitas Airlangga; CEFR C2 Certified; DET 145/160*)

---

## 💡 The Problem: The "Static Mock Test Fatigue" Dilemma

Students preparing for high-stakes international examinations frequently encounter a structural learning plateau:

```
[Static PDF Mock Papers] ──> Candidates memorize letter keys (A-C-B-D) after 2 runs
                         ──> Zero diagnostic feedback; grading consumes 40+ min per student
                         ──> Uncalibrated, subjective scoring

[Commercial Web Platforms] ──> Exorbitant recurring test tokens ($15–$35 per attempt)
                           ──> Clumsy desktop-only interfaces; fails on student phones
                           ──> Flat, robotic audio recordings lacking authentic communicative friction
```

### Why Conventional Tools Fall Short:
1. **The Memorization Trap**: In intensive test preparation cohorts, candidates exhaust standard practice tests within weeks. Subsequent attempts measure memory of previous answer keys rather than genuine linguistic competence.
2. **Tutor Bandwidth Drain**: Instructors spend 30 to 45 minutes manually marking objective reading and listening keys, leaving minimal classroom time for high-impact writing coaching and personalized diagnostic debriefs.
3. **The Acoustic Deficit**: Commercial practice materials routinely rely on sterile, over-enunciated studio recordings. When candidates face authentic native discourse containing conversational self-repair, interruptions, and regional accents (British, Australian, American), their comprehension collapses.

---

## ⚡ The Solution: Institutional-Grade Procedural Simulation

This platform replaces static practice sets with an **adaptive, client-side procedural engine** engineered to deliver infinite, psychometrically calibrated mock examinations with **zero recurring software fees**:

- **Procedural Combinatorics**: Samples from an extensive item bank featuring 5 distinct variants across 9 Reading task types, 6 Listening task structures (30 unique audio productions), and 8 curated Writing prompt pairs.
- **Deterministic Seed Engine**: Employs a deterministic Mulberry32 Pseudo-Random Number Generator. Any 6-digit seed (e.g., `#849201` or `UNAIR-B2`) constructs the exact same exam permutation across multiple devices without requiring backend database coordination.
- **Dynamic Option Permutation**: Every question dynamically shuffles its multiple-choice alternatives using Fisher-Yates randomization, remapping scoring keys and distractors on the fly. Candidates can never memorize static position patterns.
- **Instant Diagnostic Breakdown**: Immediately scores all 52 objective items, calculates the candidate's CEFR Band (A2 to C1), and surfaces item-by-item linguistic rationales explaining why target answers are correct and why distractors fail.
- **One-Tap Tutor Export**: Candidates can copy their full diagnostic log—including timestamps, sectional scores, essay drafts, word counts, and error autopsies—to send directly to their instructor via messaging channels.

---

## 🚀 Live Demonstration & Seed Presets

Launch the simulator immediately in any modern browser:

| Exam Configuration | Direct Access Link | Focus & Thematic Domain |
| :--- | :--- | :--- |
| **Fresh Procedural Exam** | [Launch Random Exam](https://prime-prmrch.github.io/cest-mock/test.html) | Dynamically assembled from verified bank |
| **Curated Seed #101** | [Seed #101 (Commercial / Workplace)](https://prime-prmrch.github.io/cest-mock/test.html?seed=101) | Corporate logistics, office leasing, retail management |
| **Curated Seed #202** | [Seed #202 (Narrative & Literary)](https://prime-prmrch.github.io/cest-mock/test.html?seed=202) | Speleology, acoustic architecture, artisan crafts |
| **Curated Seed #303** | [Seed #303 (Ecology & Earth Systems)](https://prime-prmrch.github.io/cest-mock/test.html?seed=303) | Glacial hydrology, marine restoration, ancient shipwrecks |

---

## 📐 Examination Architecture

The test adheres strictly to Cambridge general skills assessment specifications across a timed **90-minute format**:

```
TOTAL TIME: 90 MINUTES  ──┬── Reading: 33 Items (9 Distinct Tasks)
                          ├── Listening: 19 Items (6 Neural Audio Tasks, Strict 2-Play Limit)
                          └── Writing: 2 Tasks (Part 1: 150w Communicative, Part 2: 220w Feature Essay)
```

| Section | Tasks & Formats | Questions | Evaluated Core Competencies |
| :--- | :--- | :---: | :--- |
| **Reading** | Public Notices (T1), Sentence Cloze (T2), Open Cloze (T3), Vocab Cloze (T4), Extended Text (T5), Short Article (T6), Gapped Sentences (T7), Gapped Paragraphs (T8), Multiple Matching (T9) | **33 Qs** | Macro-discourse cohesion, grammatical functors, collocations, rhetorical organization, inference, and scanning. |
| **Listening** | Short Transactional (T1), Workplace Exchange (T2), Extended Interview (T3), Multi-Speaker Discussion (T4), Multiple Matching (T5), Monologue Gap Fill (T6) | **19 Qs** | Multi-accent connected speech decoding, conversational self-repair, distractor reversals, and precise numerical extraction. |
| **Writing** | Task 1: Communicative/Narrative (150–180 words)<br>Task 2: Discursive/Feature Essay (220–260 words) | **2 Tasks** | Lexical range, register control, syntactic variety, rhetorical hedging, and argument structure under timed pressure. |

---

## 🎙️ Authentic Neural Listening Bank (30 Tracks)

All listening tracks were synthesized using high-fidelity Edge-TTS neural models configured with authentic regional accents (`en-GB-SoniaNeural`, `en-GB-RyanNeural`, `en-AU-NatashaNeural`, `en-US-GuyNeural`), featuring real-world conversational dynamics:

1. **Task 1: Transactional Exchanges** — Logistics freight rerouting, equipment warranty delays, bespoke office layout fire-exit compliance.
2. **Task 2: Workplace Negotiations** — Database migration delays, retail shift substitutions, corporate mug deposit sanitation logistics.
3. **Task 3: Professional In-Depth Interviews** — Municipal soundscape engineering, speleological archaeology, modular electronics repairability.
4. **Task 4: Multi-Speaker Debates** — Designer garment rentals vs. dry cleaning, procedural game narratives vs. linear storytelling, civic assembly in privatized plazas.
5. **Task 5: 5-Speaker Thematic Matching** — Marathon motivations, mid-life artisan career transitions, urban-to-rural relocations.
6. **Task 6: Specialized Monologue Note-Taking** — Coral micro-fragmentation, Kronan-Nord Baltic shipwreck preservation, airport baggage routing systems.

*Constraint Enforcement*: Each track enforces a strict **2-play maximum** with live playback progress, replicating official Cambridge examination security protocols.

---
## 📈 CEFR Diagnostic Banding Matrix

Scoring is calibrated across the **52 objective items** (Reading 33 + Listening 19):

| Combined Score (52) | Reading Raw (33) | Listening Raw (19) | CEFR Band | Pedagogical Diagnostic Rationale |
| :---: | :---: | :---: | :---: | :--- |
| **46 – 52** | 29 – 33 | 17 – 19 | **C1 (Advanced)** | Fluent decoding of acoustic reversals, macro-cohesion, and low-frequency idiomatic lexis. Ready for C1 writing polish. |
| **38 – 45** | 24 – 28 | 14 – 16 | **B2 (Vantage)** | Confident communicative competence. Occasional vulnerability to complex hypotactic sentence gaps and acoustic distractors. |
| **28 – 37** | 18 – 23 | 10 – 13 | **B1 (Threshold)** | Reliable functional comprehension. Requires systematic practice with gapped paragraphs and lexical collocations. |
| **18 – 27** | 11 – 17 | 7 – 9 | **A2 (Waystage)** | Foundational grasp of explicit communicative exchanges. Needs reinforcement in discourse functors and connected speech. |
| **Below 18** | 0 – 10 | 0 – 6 | **Pre-A2** | Foundational linguistic remediation required before standardized multi-level testing. |

---

## 📱 Offline Resilience & Mobile PWA

The simulator is built as a standalone **Progressive Web App (PWA)** prioritizing mobile ergonomics and connection tolerance:

- **Service Worker Architecture (`sw.js`)**: Automatically pre-caches the complete application shell and test data bank (`bank.json`).
- **Commute-Ready Audio Caching**: Queues background downloads of all 30 audio tracks, allowing students to complete fully functional, multi-accent listening tests offline on trains or buses.
- **Fail-Safe Session Recovery**: Anchors test timers to true wall-clock completion timestamps (`targetEndTime`) and synchronizes state in `localStorage`. Accidental page refreshes, low-bandwidth reconnects, or incoming phone calls preserve the exact seed, candidate inputs, and elapsed countdown without resetting the session.
- **Mobile Touch Standards**: Form inputs enforce $\ge 16\text{px}$ font sizes to eliminate unwanted iOS Safari viewport zoom jumps; all touch targets maintain $\ge 48\text{px}$ hit dimensions.

---

## 📚 Master Coaching Guides

The repository includes pedagogical and instructional guides in [`guides/`](guides/):

- [Writing Mastery Guide](guides/WRITING_MASTERY_GUIDE.md): CEFR analytical rubrics, syntactic models, and cohesion strategies for narrative and discursive essays.
- [Reading & Listening Explanations](guides/READING_AND_LISTENING_EXPLANATIONS.md): Item-by-item diagnostic rationales, distractor anatomy, and rhetorical markers across all item bank tasks.
- [Test Specification & Coaching Guide](guides/TEST_SPEC_AND_COACHING_GUIDE.md): Syllabus alignments, time allocation protocols, and diagnostic interview workflows.

---

## 🛠️ Local Development & Bank Tooling

```bash
# Clone repository
git clone https://github.com/prime-prmrch/cest-mock.git
cd cest-mock

# Launch local testing server
python -m http.server 8080
# Open http://localhost:8080 in your browser

# Audio Synthesis Tooling (Edge-TTS)
cd tools
pip install -r requirements.txt
python build_bank.py
python synthesize_bank_audio.py
```

---

## 🏛️ Institutional & Portfolio Attribution

Developed and maintained by **Febrian Dhani Hartawan** as an applied educational technology and assessment architecture project.

- **Institution**: Universitas Airlangga (UNAIR), Department of English Language and Literature
- **Specialization**: IUP UNAIR Admissions Strategy, Critical Discourse Analysis, and CEFR Assessment Design
- **Portfolio Repository**: [https://github.com/prime-prmrch/cest-mock](https://github.com/prime-prmrch/cest-mock)
- **Live Simulator**: [https://prime-prmrch.github.io/cest-mock/](https://prime-prmrch.github.io/cest-mock/)
