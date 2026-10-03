# Cambridge English Skills Test (General) — Procedural Diagnostic Suite

An interactive, responsive procedural test preparation and diagnostic suite calibrated to the official **Cambridge English Skills Test (General Category)** specifications.

**Live Application**: [https://prime-prmrch.github.io/cest-mock/](https://prime-prmrch.github.io/cest-mock/)

Designed for high-stakes coaching and candidate diagnostic assessment across **mobile devices (iOS Safari PWA)** and **Windows desktop/laptop** browsers.

---

## 🎯 Test Suite Overview

Every session procedurally constructs a complete, psychometrically calibrated mock examination assessing communicative competence across **CEFR Levels A2 to C1**:

| Component | Tasks & Structure | Items / Timing | Format & Design |
| :--- | :--- | :---: | :--- |
| **Reading** | Notices (T1), Sentence Cloze (T2), Open Cloze (T3), Vocab Cloze (T4), Extended Text (T5), Short Article (T6), Gapped Sentences (T7), Gapped Paragraphs (T8), Multiple Matching (T9) | **33 Questions** | Authentic communicative, commercial, literary, and scientific registers sampled from the item bank. |
| **Listening** | Short Transactional Dialogue (T1), Workplace Exchange (T2), Extended Interview (T3), Multi-Speaker Discussion (T4), Multiple Matching (T5), Sentence Completion (T6) | **19 Questions** | Diverse native accents (British, Australian, American) synthesized via Edge-TTS neural voices, enforcing an authentic **2-play maximum audio limit**. |
| **Writing** | Part 1: Communicative/Narrative Task (150–180 words)<br>Part 2: Feature Essay/Article (220–260 words) | **2 Tasks** | Dedicated **45-minute countdown**, live word count monitoring, and local storage auto-save. |

*Speaking is excluded in accordance with targeted coaching specifications.*

---

## 🎲 Procedural Exam Generator & Seed Synchronization

Instead of a static set of fixed papers, the simulator features a **client-side procedural assembler** driven by a deterministic Mulberry32 Pseudo-Random Number Generator:

- **Instant Random Exam**: Clicking **"Launch Fresh Random Exam"** generates a fresh 6-digit seed (e.g., `#849201`), assembling a unique test configuration in milliseconds with zero server latency.
- **Tutor & Candidate Synchronization**: Enter any custom alphanumeric seed (e.g., `UNAIR-B2-01` or `748291`) to generate the identical test across different devices for homework or synchronized mock exam sessions.
- **One-Tap Share Link**: Tutors can tap **"Share Seed"** directly in the test header to copy the exact URL (`test.html?seed=XYZ`) to the clipboard.
- **Combinatorics**: With 5 variants across all 6 listening task slots and modular reading pools, candidates can take thousands of distinct exams without repetitive item fatigue.
---
## 📈 CEFR Diagnostic Banding Matrix

Scoring is calibrated across the **52 objective items** (Reading 33 + Listening 19):

| Combined Score (out of 52) | Reading Raw (33) | Listening Raw (19) | Indicated CEFR Level | Pedagogical Diagnostic Summary |
| :---: | :---: | :---: | :---: | :--- |
| **46 – 52** | 29 – 33 | 17 – 19 | **C1 (Advanced)** | Mastered macro-cohesion, subtle acoustic reversals, and low-frequency lexis. Ready for C1 writing polish. |
| **38 – 45** | 24 – 28 | 14 – 16 | **B2 (Vantage / Independent)** | Solid competence with communicative English. Requires practice on complex multi-clause sentence gaps. |
| **28 – 37** | 18 – 23 | 10 – 13 | **B1 (Threshold / Intermediate)** | Good baseline comprehension. Vulnerable to distractor reversals in listening and academic cloze collocations. |
| **18 – 27** | 11 – 17 | 7 – 9 | **A2 (Waystage)** | Requires systematic reinforcement of core grammatical functors and connected speech decoding. |
| **Below 18** | 0 – 10 | 0 – 6 | **Below A2** | Foundational English remediation required prior to standardized multi-level assessment. |

---

## 📖 Master Coaching & Pedagogical Guides

Comprehensive documentation for tutors, examiners, and candidates located in [`guides/`](guides/):

- [Writing Mastery Guide](guides/WRITING_MASTERY_GUIDE.md): Structural templates, CEFR A2–C1 assessment rubrics, cohesion mechanics, and lexical banks for Task 1 (Narrative) and Task 2 (Discursive/Feature Essay).
- [Reading & Listening Explanations](guides/READING_AND_LISTENING_EXPLANATIONS.md): Item-by-item diagnostic rationales, distractor anatomy, and discourse markers for all objective items across the test bank.
- [Test Specification & Coaching Guide](guides/TEST_SPEC_AND_COACHING_GUIDE.md): Institutional specifications, syllabus mapping, time management protocols, and diagnostic session frameworks.

---

## 📱 Progressive Web App (PWA) & Offline Caching

The application is a standalone Progressive Web App:
- **Service Worker (`sw.js`)**: Automatically pre-caches the application shell (`index.html`, `test.html`, `css/style.css`, `js/engine.js`, `js/scoring.js`, `js/procedural.js`) and `data/bank.json`.
- **Background Audio Pre-Caching**: The Service Worker pre-caches all 30 audio tracks in the background, allowing candidates to practice procedurally generated tests offline during commutes without an internet connection.
- **Home Screen Installation**:
  - **iOS Safari**: Tap **Share** $\rightarrow$ **Add to Home Screen**. Launches in standalone fullscreen mode without browser URL chrome.
  - **Android / Chrome / Desktop**: Tap the install badge in the address bar or select **Install App** from the browser menu.
- **Touch Ergonomics**: All input targets maintain $\ge 16\text{px}$ font sizes to eliminate iOS viewport zoom jumps; buttons and controls maintain $\ge 48\text{px}$ hit areas.

---

## 🛠️ Local Development & Audio Generation

```bash
# Clone and enter repo
git clone https://github.com/prime-prmrch/cest-mock.git
cd cest-mock

# Run local web server
python -m http.server 8080
# Open http://localhost:8080 in your browser

# Audio Tooling (Edge-TTS)
cd tools
pip install -r requirements.txt
python build_bank.py
python synthesize_bank_audio.py
```
