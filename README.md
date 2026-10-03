# Cambridge English Skills Test (General) — Procedural Diagnostic Suite

[![Live Portal](https://img.shields.io/badge/Live%20Portal-GitHub%20Pages-0077b6?style=flat-square)](https://prime-prmrch.github.io/cest-mock/)
[![Engine](https://img.shields.io/badge/Engine-Procedural%20PRNG-blueviolet?style=flat-square)](#-procedural-exam-generator--seed-synchronization)
[![PWA](https://img.shields.io/badge/PWA-Full%20Offline%20Ready-success?style=flat-square)](#-progressive-web-app-pwa--offline-caching)
[![TTS Engine](https://img.shields.io/badge/Audio-30%20Neural%20Tracks-purple?style=flat-square)](#-expanded-neural-listening-bank-30-tracks)

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

### Standard Seed Presets
- [Seed #101 (Baseline Commercial)](https://prime-prmrch.github.io/cest-mock/test.html?seed=101)
- [Seed #202 (Narrative & Literary)](https://prime-prmrch.github.io/cest-mock/test.html?seed=202)
- [Seed #303 (Ecology & Deep Time)](https://prime-prmrch.github.io/cest-mock/test.html?seed=303)

---

## 🎙️ Expanded Neural Listening Bank (30 Tracks)

All listening tasks feature authentic communicative friction, conversational self-repair, and conceptual paraphrasing—eliminating superficial "lost-and-found" tropes:

1. **Task 1: Short Transactional Dialogues (Q1)**
   - *V1 Transit*: Rail line maintenance, replacement coach congestion vs. scenic rail detour.
   - *V2 Warranty*: Hardware phantom power failure; direct replacement vs. 10-day diagnostic inspection delay.
   - *V3 Logistics*: Regional showroom freight delay; redirecting delivery to industrial depot for morning pickup.
   - *V4 Furniture*: Bespoke office meeting pod; swapping rectangular tables to circular profiles to clear fire exits.
   - *V5 Catering*: Corporate workshop booking; meeting lunch package threshold to waive room hire charges.

2. **Task 2: Collaborative Workplace Discussions (Q2)**
   - *V1 Systems*: Database connector delay; hiring temporary data clerks to manage manual records backlog.
   - *V2 Retail*: Weekend inventory flu absences; swapping shifts with restocking crew to avoid overtime penalties.
   - *V3 Marketing*: Digital display banner ROI failure; reallocating budget to industry technical newsletters.
   - *V4 Eco-Scheme*: Reusable coffee mug deposit scheme; mitigating sanitization concerns with high-temp dishwashers.
   - *V5 Licensing*: Enterprise software contracts; opting for rolling quarterly terms to accommodate restructuring.

3. **Task 3: Extended Professional Interviews (Q3–Q7)**
   - *V1*: Marcus Thorne on municipal acoustic architecture and civic soundscape design.
   - *V2*: Dr. Julian Croft on exploratory Yucatan speleology and prehistoric cave archaeology.
   - *V3*: Dr. Naomi Chen on Patagonian glacial acoustics and bio-acoustic ecosystem health.
   - *V4*: Rachel Vance on nationwide cold-chain logistics, EV truck cooling draw, and warehouse robotics.
   - *V5*: David Cho on modular appliance design, fighting planned obsolescence, and right-to-repair laws.

4. **Task 4: Multi-Speaker Discussions (Q8–Q9)**
   - *V1*: Designer garment rental subscriptions vs. dry-cleaning logistics.
   - *V2*: Emergent player-driven storytelling vs. pre-scripted game narrative pacing.
   - *V3*: Privatized commercial plazas vs. democratic civic public assembly.
   - *V4*: Mandatory three-day corporate office attendance vs. quiet analytical remote work.
   - *V5*: Supermarket self-checkout automation vs. cashier customer goodwill.

5. **Task 5: 5-Speaker Multiple Matching (Q10–Q14)**
   - *V1*: Personal motivations for marathon distance running (escapism, health scare, social club, race splits, travel).
   - *V2*: Mid-life career transitions (offshore sailing, sensory gardening, physics teaching, artisan bakery, rare books).
   - *V3*: Serendipitous career pivots (Pyrenees rescue dog, Tuscan cello luthier, antique botanist letter, Newcastle letterpress, Hebridean dialect).
   - *V4*: Deciding to change commute methods (e-bike mental buffer, park-and-ride costs, carpooling camaraderie, walking for claustrophobia, off-peak rail table space).
   - *V5*: Relocating from metropolises to small towns (affordable family garden, caregiving elderly parents, mountain hiking access, independent coffee roastery, escaping 3-hour transit).

6. **Task 6: Monologue Sentence Completion (Q15–Q19)**
   - *V1*: Coral reef micro-fragmentation and marine ecosystem restoration.
   - *V2*: The 17th-century Kronan-Nord Baltic shipwreck and anoxic wood preservation.
   - *V3*: Celtic rainforest temperate Atlantic woodland lichens as pollution bio-indicators.
   - *V4*: Automated airport baggage handling networks, RFID tags, CT scanners, and aircraft turnaround metrics.
   - *V5*: Municipal wastewater recycling facilities, membrane bioreactors, reverse osmosis, and industrial cooling towers.

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
