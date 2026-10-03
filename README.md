# Cambridge English Skills Test (General) — Diagnostic Practice Suite

[![Live Portal](https://img.shields.io/badge/Live%20Portal-GitHub%20Pages-0077b6?style=flat-square)](https://prime-prmrch.github.io/cest-mock/)
[![PWA](https://img.shields.io/badge/PWA-Offline%20Ready-success?style=flat-square)](#-progressive-web-app-pwa--offline-caching)
[![TTS Engine](https://img.shields.io/badge/Audio-Edge--TTS%20Neural-purple?style=flat-square)](#-audio-synthesis-tooling)

An interactive, responsive multi-test preparation and diagnostic suite calibrated to the official **Cambridge English Skills Test (General Category)** specifications.

**Live Application**: [https://prime-prmrch.github.io/cest-mock/](https://prime-prmrch.github.io/cest-mock/)

Designed specifically for coaching and student assessment across **mobile devices (iOS Safari)** and **Windows desktop/laptop** browsers.

---

## 🎯 Test Suite Overview

This repository provides three complete, distinct mock examinations assessing communicative competence across **CEFR Levels A2 to C1** across three non-speaking components:

| Component | Tasks & Structure | Items / Timing | Format & Design |
| :--- | :--- | :---: | :--- |
| **Reading** | Notices, Sentence Cloze, Open Cloze, Vocab Cloze, Extended Text, Short Article, Gapped Sentences, Gapped Paragraphs, Multiple Matching | **33 Questions** | Authentic communicative, literary, and scientific registers. |
| **Listening** | Short Dialogues, Extended Interviews, Multi-Speaker Discussions, Multiple Matching, Sentence Completion | **19 Questions** | Diverse native accents (British, Australian, American) synthesized via Edge-TTS neural voices, enforcing an authentic **2-play maximum audio limit**. |
| **Writing** | Part 1: Communicative/Narrative Task (150–180 words)<br>Part 2: Feature Essay/Article (220–260 words) | **2 Tasks** | Dedicated **45-minute countdown**, live word count monitoring, and local storage auto-save. |

*Speaking is strictly excluded in accordance with targeted coaching specifications.*

---

## 📚 Mock Test Modules

The test suite is powered by a decoupled frontend engine (`test.html`, `js/engine.js`, `js/scoring.js`, `css/style.css`) driven by JSON data configurations (`data/index.json`, `mock_test_1/test_data.json`, `mock_test_2/test_data.json`, `mock_test_3/test_data.json`), with automatic local state persistence.

### 📘 [Mock Test 1: General Adaptive Baseline](https://prime-prmrch.github.io/cest-mock/test.html?id=1)
- **Reading Themes**: Deep-sea autonomous robotics, Elena Vance's wildlife cinematography, marine bioluminescence, acoustic ecology in city squares.
- **Listening Tracks**: Lost property at a cafe, professional scheduling workshop, Marcus Thorne acoustic architecture interview, sustainable fashion rental debate, 5 runner monologues, coral reef micro-fragmentation restoration.
- **Writing**: Part 1 Narrative letter on an unexpected 1880s botanical field journal discovered in a coastal library archive; Part 2 Critical feature article on *"The Lost Art of Browsing: Why Physical Bookshops and Uncurated Shelves Matter in a Digital Age"*.

### 🎨 [Mock Test 2: Narrative & Literary Horizons](https://prime-prmrch.github.io/cest-mock/test.html?id=2)
- **Reading Themes**: Antiquarian Manuscript Reading Room rules, Hay-on-Wye book town origins, traditional boxwood engraving, Dartmoor granite solitude travel memoir, olfactory neuroscience (Proustian phenomenon), Renaissance phantom islands (Hy-Brasil), revival of hand-penned fountain pen letters, four master antique restorers (horologist, bookbinder, pipe organ voicer, stained-glass glazier).
- **Listening Tracks**: Lost leather sketchbook on Edinburgh express, kitchen power outage and wood-fired cooking adaptation, Dr. Julian Croft subterranean cenote speleology interview, Marcus and Elena on emergent video game storytelling, 5 mid-life career transition accounts, Dr. Maya Lin on the 17th-century Kronan-Nord Baltic shipwreck.
- **Writing**: Part 1 Narrative letter recounting an unexpected storm sanctuary in a historic Welsh watermill bookbindery; Part 2 Critical literary essay on *"The Voice and the Page: Audiobooks and the Architecture of Reading"*.

### 🌿 [Mock Test 3: Atmospheric Ecology & Deep Time](https://prime-prmrch.github.io/cest-mock/test.html?id=3)
- **Reading Themes**: Movable letterpress studio regulations, Saint Paul's Cathedral whispering gallery wave physics, alchemy of Renaissance lapis lazuli pigments, Arctic glaciology field memoir on Nordenskiöld Glacier, cognitive value of solitude (default mode network), medieval monastic scriptoria labor and colophons, European river re-wilding and beaver hydrology, four literary translators on preserving cultural texture and voice.
- **Listening Tracks**: Antique brass navigational compass in botanical conservatory, architects evaluating a 4-day working week pilot, Naomi Chen Patagonian glacial acoustic ecology interview, privatized commercial plazas debate, 5 serendipitous career pivot accounts, Dr. Alistair MacIntyre on temperate Celtic rainforest lichens and bio-indicators.
- **Writing**: Part 1 Narrative field dispatch reporting an extraordinary nocturnal fall of exhausted migrant songbirds in fog at a coastal bird observatory; Part 2 Discursive essay on *"The Reclamation of Darkness: Artificial Light, Ecology, and the Lost Night Sky"*.

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
- [Reading & Listening Explanations](guides/READING_AND_LISTENING_EXPLANATIONS.md): Item-by-item diagnostic rationales, distractor anatomy, and discourse markers for all 52 objective items across Mock Tests 1–3.
- [Test Specification & Coaching Guide](guides/TEST_SPEC_AND_COACHING_GUIDE.md): Institutional specifications, syllabus mapping, time management protocols, and diagnostic session frameworks.

---

## 📱 Progressive Web App (PWA) & Offline Caching

The application is a fully configured Progressive Web App:
- **Service Worker (`sw.js`)**: Automatically pre-caches the application shell (`index.html`, `test.html`, `css/style.css`, `js/engine.js`, `js/scoring.js`) and all test JSON data.
- **On-Demand Audio Caching**: Audio tracks are dynamically cached upon initial playback, enabling offline practice during commutes or low-connectivity environments.
- **Home Screen Installation**:
  - **iOS Safari**: Tap the **Share** button $\rightarrow$ **Add to Home Screen**. Launches in standalone fullscreen mode without browser URL chrome.
  - **Android / Chrome / Desktop**: Tap the install badge in the address bar or select **Install App** from the browser menu.
- **Mobile Touch Optimization**: Inputs maintain $\ge 16\text{px}$ font size to avoid iOS zoom jumps; buttons and controls maintain $\ge 48\text{px}$ touch targets.

---

## 🎙️ Audio Synthesis Tooling

The audio generation scripts are housed in [`tools/`](tools/), utilizing Microsoft `edge-tts` neural voices (`en-GB-SoniaNeural`, `en-GB-RyanNeural`, `en-GB-LibbyNeural`, `en-AU-NatashaNeural`, `en-US-JennyNeural`, etc.):

```bash
# Setup
cd tools
pip install -r requirements.txt

# Verify or regenerate all mock test listening audio
python generate_mock_audio.py

# Force re-synthesis
python generate_mock_audio.py --force

# Custom voice synthesis
python voice_gen.py speak --text "Cambridge English Skills Test." --voice en-GB-RyanNeural --output test.mp3
```

---

## 🛠️ Local Development

To run the simulator locally:
```bash
# Double-click run_mock_test.bat (Windows) or execute via shell:
python -m http.server 8080
```
Open `http://localhost:8080` in your web browser.
