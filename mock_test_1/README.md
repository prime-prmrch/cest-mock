# Cambridge English Skills Test (General) — Mock Test 1 Simulator

An interactive, responsive web simulator and diagnostic test pack calibrated to the official **Cambridge English Skills Test (General Category)** specifications.

Designed specifically for seamless coaching and student preparation on **mobile devices (iOS Safari)** and desktop browsers.

---

## 🎯 Test Structure & Coverage

This simulator assesses communicative competence across **CEFR Levels A2 to C1** across three non-speaking components:

| Section | Tasks | Items | Timing & Mechanics |
| :--- | :--- | :---: | :--- |
| **Section 1: Reading** | Notices, Sentence Cloze, Open Cloze, Vocab Cloze, Extended Text, Short Article, Gapped Sentences, Gapped Paragraphs, Multiple Text Matching | **33 Questions** | Diagnostic reading comprehension across diverse registers (informal to academic). |
| **Section 2: Listening** | Picture Choice, Short Dialogue, Extended Interview, Multi-Speaker Discussion, Multiple Matching, Sentence Completion | **19 Questions** | Features diverse native accents (British, Australian, American) with an authentic **2-play maximum audio limit**. |
| **Section 3: Writing** | Part 1: Informal Email (min. 50 words)<br>Part 2: Civic Forum Post (min. 180 words) | **2 Tasks** | Dedicated **45-minute countdown**, live word counter, and keystroke auto-save to local storage. |

*Note: Speaking is excluded per targeted coaching specifications.*

---

## ✨ Features

- **📱 iOS Safari Optimized**: 
  - Strict $\ge 16\text{px}$ inputs prevent automatic screen zoom upon keyboard activation.
  - Touch-friendly 48px target heights and safe-area inset spacing.
  - Can be added directly to the iPhone Home Screen as a standalone, distraction-free web app.
- **🎧 Real-Time Audio Constraints**: Audio players track playback counts and automatically disable after 2 listens to replicate genuine Cambridge test conditions.
- **📊 Instant Diagnostic Scoring**: Automated raw score calculation out of 52 with empirical conversion to CEFR levels (Below A2, A2, B1, B2, C1).
- **💡 3-Tier Coach Rationales**: Item-by-item breakdown detailing the correct answer, distractor trap analysis, and targeted CEFR linguistic skill.
- **📋 One-Tap Coach Sharing**: Students can instantly copy their complete diagnostic performance, error log, and written responses to the clipboard to share with their instructor.

---

## 📈 CEFR Diagnostic Banding Matrix

| Combined Raw Score (out of 52) | Reading (33) | Listening (19) | Indicated CEFR Level |
| :---: | :---: | :---: | :---: |
| **46 – 52** | 29 – 33 | 17 – 19 | **C1 (Advanced)** |
| **38 – 45** | 24 – 28 | 14 – 16 | **B2 (Vantage / Independent)** |
| **28 – 37** | 18 – 23 | 10 – 13 | **B1 (Threshold / Intermediate)** |
| **18 – 27** | 11 – 17 | 7 – 9 | **A2 (Waystage)** |
| **Below 18** | 0 – 10 | 0 – 6 | **Below A2** |

---

## 🛠️ Offline / Local Deployment

To run this test locally without internet:
```bash
python -m http.server 8080
# or
npx serve -l 8080
```
Then navigate to `http://localhost:8080` (or `http://<your-local-ip>:8080` on local mobile Wi-Fi).
