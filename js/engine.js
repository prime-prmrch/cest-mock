/**
 * Cambridge English Skills Test (General)
 * Unified Interactive Test Runner Engine
 */

let currentTestData = null;
let currentTestId = 1;
const audioPlays = {};
let timerInterval = null;

document.addEventListener('DOMContentLoaded', () => {
  initEngine();
});

async function initEngine() {
  const urlParams = new URLSearchParams(window.location.search);
  const seedParam = urlParams.get('seed');
  const idParam = urlParams.get('id');

  // Procedural is the primary mode
  const isArchival = Boolean(idParam && [1, 2, 3].includes(parseInt(idParam)));
  let activeSeed = seedParam ? seedParam.trim() : String(Math.floor(100000 + Math.random() * 900000));

  try {
    if (!isArchival) {
      // Ensure procedural script is dynamically loaded if not already present
      if (!window.CESTProcedural) {
        await new Promise((resolve, reject) => {
          const s = document.createElement('script');
          s.src = `js/procedural.js?v=5`;
          s.onload = resolve;
          s.onerror = () => reject(new Error('Failed to load procedural library'));
          document.head.appendChild(s);
        });
      }

      const res = await fetch('data/bank.json?v=5');
      if (!res.ok) throw new Error(`HTTP ${res.status}: Failed to load bank.json.`);
      const bank = await res.json();
      currentTestData = window.CESTProcedural.assembleTest(bank, activeSeed);
      currentTestId = activeSeed;
      updatePortalNavProcedural(activeSeed);
    } else {
      currentTestId = parseInt(idParam);
      updatePortalNav(currentTestId);
      const res = await fetch(`data/test_${currentTestId}.json?v=4`);
      if (!res.ok) throw new Error(`HTTP ${res.status}: Failed to load test data.`);
      currentTestData = await res.json();
    }

    renderExam(currentTestData);
    loadSavedState();
    startTimer((currentTestData.durationMinutes || 90) * 60);
  } catch (err) {
    console.error("Test initialization error:", err);
    document.querySelector('.container').innerHTML = `
      <div class="task-card" style="text-align:center; padding:40px 20px;">
        <h2 style="color:var(--danger); margin-bottom:12px;">Failed to Load Test Data</h2>
        <p style="color:var(--text-muted); margin-bottom:20px;">Could not retrieve test content. Please verify data files and reload.</p>
        <a href="index.html" class="btn btn-primary" style="display:inline-block;">Return to Portal Hub</a>
      </div>
    `;
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
      <button type="button" onclick="copySeedLink('${escapeHtml(seed)}')" style="background:var(--secondary); color:white; border:none; border-radius:4px; padding:4px 10px; font-size:11px; font-weight:700; cursor:pointer;">🔗 Share Seed</button>
      <a href="test.html" style="background:#f1f5f9; color:var(--text); text-decoration:none; border-radius:4px; padding:4px 10px; font-size:11px; font-weight:700;">🔄 New Random</a>
    </div>
  `;
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

  // Render Reading Tasks
  const rContainer = document.getElementById('section-reading');
  if (rContainer && data.reading) {
    rContainer.innerHTML = data.reading.map(task => renderReadingTask(task)).join('');
  }

  // Render Listening Tasks
  const lContainer = document.getElementById('section-listening');
  if (lContainer && data.listening) {
    lContainer.innerHTML = data.listening.map(task => renderListeningTask(task, data.audioDir)).join('');
  }

  // Render Writing Tasks
  const wContainer = document.getElementById('section-writing');
  if (wContainer && data.writing) {
    wContainer.innerHTML = data.writing.map(task => renderWritingTask(task)).join('');
  }

  // Attach event listeners for inputs
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
        <button type="button" class="play-btn" id="${btnId}" onclick="playAudio('${audioId}', '${btnId}', '${badgeId}', '${progId}', '${timeId}')">&#9658;</button>
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
      <label class="option-card" onclick="selectOption(this)">
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
  const minWords = task.minWords || 150;

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
      <textarea class="essay-textarea" id="${textId}" placeholder="Compose your response here..." oninput="handleWritingInput('${textId}', '${badgeId}', ${minWords})"></textarea>
      <div class="writing-footer">
        <span class="word-count-badge" id="${badgeId}">0 words (Min: ${minWords})</span>
        <button type="button" class="btn btn-secondary" style="padding:6px 12px; font-size:13px;" onclick="copySingleWriting('${textId}', '${escapeHtml(task.title)}')">Copy Draft</button>
      </div>
    </div>
  `;
}

// --- NAVIGATION & TABS ---
function switchSection(secId) {
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
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

// --- OPTION SELECTION ---
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

// --- AUDIO CONTROLLER ---
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
    const remaining = state.max - state.count;
    badge.innerText = "Plays left: " + remaining;
    if (remaining === 0) badge.classList.add('depleted');
  }

  // Stop any other active audios
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
  };
}

// --- WRITING INPUT ---
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

// --- TIMER ---
function startTimer(durationSeconds) {
  let seconds = durationSeconds;
  const timerBadge = document.getElementById('examTimer');
  if (!timerBadge) return;

  if (timerInterval) clearInterval(timerInterval);

  timerInterval = setInterval(() => {
    seconds--;
    if (seconds < 0) {
      clearInterval(timerInterval);
      timerBadge.innerText = "00:00";
      showToast("Time has expired! Submitting test automatically...");
      submitExam();
      return;
    }
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    timerBadge.innerText = `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;

    if (seconds <= 600) {
      timerBadge.style.color = "var(--danger)";
      timerBadge.style.borderColor = "var(--danger)";
    }
  }, 1000);
}

// --- TOAST ---
function showToast(msg) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2600);
}

// --- LOCAL STORAGE STATE MANAGEMENT ---
function saveState() {
  if (!currentTestData) return;
  const state = {
    testId: currentTestId,
    candidateName: document.getElementById('candidateName')?.value || "",
    radios: {},
    texts: {},
    selects: {},
    writing: {
      part1: document.getElementById('w_part1')?.value || "",
      part2: document.getElementById('w_part2')?.value || ""
    }
  };

  document.querySelectorAll('input[type="radio"]:checked').forEach(r => {
    state.radios[r.name] = r.value;
  });

  document.querySelectorAll('.gap-text-input').forEach(inp => {
    if (inp.value) state.texts[inp.id] = inp.value;
  });

  document.querySelectorAll('.select-input').forEach(sel => {
    if (sel.value) state.selects[sel.id] = sel.value;
  });

  try {
    localStorage.setItem(`cest_mock_${currentTestId}_state`, JSON.stringify(state));
  } catch (e) {
    console.warn("Storage quota exceeded", e);
  }
}

function loadSavedState() {
  try {
    const raw = localStorage.getItem(`cest_mock_${currentTestId}_state`);
    if (!raw) return;
    const state = JSON.parse(raw);

    if (state.candidateName && document.getElementById('candidateName')) {
      document.getElementById('candidateName').value = state.candidateName;
    }

    if (state.radios) {
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

    if (state.texts) {
      for (let qid in state.texts) {
        const inp = document.getElementById(qid);
        if (inp) inp.value = state.texts[qid];
      }
    }

    if (state.selects) {
      for (let qid in state.selects) {
        const sel = document.getElementById(qid);
        if (sel) sel.value = state.selects[qid];
      }
    }

    if (state.writing) {
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
  } catch (err) {
    console.warn("Failed to load saved test state:", err);
  }
}

function attachInputListeners() {
  document.querySelectorAll('.gap-text-input').forEach(inp => {
    inp.addEventListener('input', () => {
      saveState();
      updateProgressBadge();
    });
  });

  document.querySelectorAll('.select-input').forEach(sel => {
    sel.addEventListener('change', () => {
      saveState();
      updateProgressBadge();
    });
  });

  const nameInput = document.getElementById('candidateName');
  if (nameInput) {
    nameInput.addEventListener('input', saveState);
  }
}

function countAnswered() {
  let answered = 0;
  // Radios
  const groups = new Set();
  document.querySelectorAll('input[type="radio"]').forEach(r => groups.add(r.name));
  groups.forEach(name => {
    if (document.querySelector(`input[name="${name}"]:checked`)) answered++;
  });
  // Text inputs
  document.querySelectorAll('.gap-text-input').forEach(inp => {
    if (inp.value.trim().length > 0) answered++;
  });
  // Select inputs
  document.querySelectorAll('.select-input').forEach(sel => {
    if (sel.value.length > 0) answered++;
  });
  return answered;
}

function updateProgressBadge() {
  const answered = countAnswered();
  const progEl = document.getElementById('answeredProgress');
  if (progEl) {
    progEl.innerText = `${answered} / 52 answered`;
  }
}

// --- SUBMIT EXAM ---
function submitExam() {
  if (!currentTestData) return;

  const answered = countAnswered();
  if (answered < 52) {
    const proceed = confirm(`You have completed ${answered} of 52 objective questions. Would you like to submit now and view your diagnostic evaluation?`);
    if (!proceed) return;
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
