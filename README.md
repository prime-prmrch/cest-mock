# Cambridge English Skills Test (General) — Diagnostic Practice Suite

An interactive, responsive multi-test preparation and diagnostic suite calibrated to the official **Cambridge English Skills Test (General Category)** specifications.

Designed specifically for seamless coaching and student preparation on **mobile devices (iOS Safari)** and **Windows desktop/laptop** browsers.

---

## 🎯 Test Suite Overview

This repository provides three complete, distinct mock examinations assessing communicative competence across **CEFR Levels A2 to C1** across three non-speaking components:

| Component | Tasks & Structure | Items / Timing | Format & Design |
| :--- | :--- | :---: | :--- |
| **Reading** | Notices, Sentence Cloze, Open Cloze, Vocab Cloze, Extended Text, Short Article, Gapped Sentences, Gapped Paragraphs, Multiple Matching | **33 Questions** | Rigorous reading comprehension spanning authentic communicative, literary, and scientific registers. |
| **Listening** | Short Dialogues, Extended Interviews, Multi-Speaker Discussions, Multiple Matching, Sentence Completion | **19 Questions** | Diverse native accents (British, Australian, American) with an authentic **2-play maximum audio limit**. |
| **Writing** | Part 1: Communicative/Narrative Task (150–180 words)<br>Part 2: Feature Essay/Article (220–260 words) | **2 Tasks** | Dedicated **45-minute countdown**, live word count monitoring, and local storage auto-save. |

*Speaking is strictly excluded in accordance with targeted coaching specifications.*

---

## 📚 Mock Test Modules

### 📘 [Mock Test 1: General Adaptive Baseline](mock_test_1/index.html)
- **Reading Themes**: Deep-sea autonomous robotics, Elena Vance's wildlife cinematography, marine bioluminescence, acoustic ecology in city squares.
- **Listening Tracks**: Lost property at a cafe, professional scheduling workshop, Marcus Thorne acoustic architecture interview, sustainable fashion rental debate, 5 runner monologues, coral reef micro-fragmentation restoration.
- **Writing**: Informal email for David's retirement gathering; civic forum contribution on pedestrianizing historic town centers.

### 🎨 [Mock Test 2: Narrative & Literary Horizons](mock_test_2/index.html)
- **Reading Themes**: Antiquarian Manuscript Reading Room rules, Hay-on-Wye book town history, traditional boxwood engraving, Dartmoor granite solitude travel memoir, olfactory neuroscience (Proustian phenomenon), Renaissance phantom islands (Hy-Brasil), revival of hand-penned fountain pen letters, four master antique restorers (horologist, bookbinder, pipe organ voicer, stained-glass glazier).
- **Listening Tracks**: Lost leather sketchbook on Edinburgh express, kitchen power outage and wood-fired cooking adaptation, Dr. Julian Croft subterranean cenote speleology interview, Marcus and Elena on emergent video game storytelling, 5 mid-life career transition accounts, Dr. Maya Lin on the 17th-century Kronan-Nord Baltic shipwreck.
- **Writing**: Part 1 Narrative email recounting an alpine travel misadventure, storm shelter in a shepherd's bothy, and updated arrival; Part 2 Cultural feature article on *"The Objects We Inherit: Craftsmanship, Imperfection, and Soul in an Age of Automation"*.

### 🌿 [Mock Test 3: Atmospheric Ecology & Deep Time](mock_test_3/index.html)
- **Reading Themes**: Movable letterpress studio regulations, Saint Paul's Cathedral whispering gallery wave physics, alchemy of Renaissance lapis lazuli pigments, Arctic glaciology field memoir on Nordenskiöld Glacier, cognitive value of solitude (default mode network), medieval monastic scriptoria labor and colophons, European river re-wilding and beaver hydrology, four literary translators on preserving cultural texture and voice.
- **Listening Tracks**: Antique brass navigational compass in botanical conservatory, architects evaluating a 4-day working week pilot, Naomi Chen Patagonian glacial acoustic ecology interview, privatized commercial plazas debate, 5 serendipitous career pivot accounts, Dr. Alistair MacIntyre on temperate Celtic rainforest lichens and bio-indicators.
- **Writing**: Part 1 Narrative field incident report recounting an unexpected river flash flood, bothy evacuation, and specimen preservation; Part 2 Reflective cultural essay on *"The Algorithmic Self: Serendipity and Autonomy in an Era of Predictive Feeds"*.

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

## 📱 Platform & Mobile Optimizations

- **iOS Safari / iPhone Compatibility**:
  - All input fields enforce font sizes $\ge 16\text{px}$ to eliminate automatic screen zooming when the virtual keyboard appears.
  - Interactive touch targets strictly adhere to $\ge 48\text{px}$ minimum hit areas.
  - Supports adding directly to the Home Screen (*Share &rarr; Add to Home Screen*) for a clean, distraction-free native app appearance.
- **Windows Desktop / Laptop Compatibility**:
  - Responsive container layout with sticky header navigation, persistent countdown timers, and audio progress scrubbers.
- **Real Examination Constraints**:
  - Audio tracks automatically enforce an authentic 2-play maximum limit.
- **One-Tap Coach Export**:
  - Automatically formats the student's complete objective score breakdown, item-by-item error log with pedagogical rationales, and writing submissions into a clean report ready for copying to clipboard or downloading.

---

## 🛠️ Offline / Local Deployment

To run this preparation suite locally:
```bash
# Using Python:
python -m http.server 8080

# Or using Node:
npx serve -l 8080
```
Then open `http://localhost:8080` in your web browser (or `http://<your-local-ip>:8080` on local mobile Wi-Fi).
