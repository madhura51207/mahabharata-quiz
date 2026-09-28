/**
 * Mahabharata Quiz - Main Application Controller
 * Connects the UI elements to the QuizEngine, AudioService, and GeminiService.
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // References to Services & Data
  // -------------------------------------------------------------------------
  const questionPool = window.MAHABHARATA_QUESTIONS || [];
  const engine = new QuizEngine(questionPool);
  const audio = window.audioService;
  const gemini = window.geminiService;

  // -------------------------------------------------------------------------
  // DOM Elements
  // -------------------------------------------------------------------------
  // Screens
  const homeScreen = document.getElementById('homeScreen');
  const quizScreen = document.getElementById('quizScreen');
  const resultsScreen = document.getElementById('resultsScreen');

  // Setup Form
  const quizSetupForm = document.getElementById('quizSetupForm');
  const generateQuizBtn = document.getElementById('generateQuizBtn');
  const brandHomeBtn = document.getElementById('brandHomeBtn');

  // Header Actions
  const soundToggleBtn = document.getElementById('soundToggleBtn');
  const soundIcon = document.getElementById('soundIcon');
  const aiSettingsBtn = document.getElementById('aiSettingsBtn');
  const openAiModalBtn = document.getElementById('openAiModalBtn');
  const aiGenerateBtn = document.getElementById('aiGenerateBtn');

  // Active Quiz View
  const badgeAge = document.getElementById('badgeAge');
  const badgeCategory = document.getElementById('badgeCategory');
  const badgeDifficulty = document.getElementById('badgeDifficulty');
  const badgeAiMode = document.getElementById('badgeAiMode');
  const timerDisplay = document.getElementById('timerDisplay');
  const quitQuizBtn = document.getElementById('quitQuizBtn');
  const currentQNum = document.getElementById('currentQNum');
  const totalQNum = document.getElementById('totalQNum');
  const progressPercent = document.getElementById('progressPercent');
  const progressBarFill = document.getElementById('progressBarFill');
  const questionCategoryTag = document.getElementById('questionCategoryTag');
  const questionAgeTag = document.getElementById('questionAgeTag');
  const activeQuestionText = document.getElementById('activeQuestionText');
  const optionsContainer = document.getElementById('optionsContainer');
  const prevQuestionBtn = document.getElementById('prevQuestionBtn');
  const nextQuestionBtn = document.getElementById('nextQuestionBtn');
  const nextBtnLabel = document.getElementById('nextBtnLabel');

  // Results View
  const resultBadgeIcon = document.getElementById('resultBadgeIcon');
  const resultTitle = document.getElementById('resultTitle');
  const resultSubtitle = document.getElementById('resultSubtitle');
  const statTotalScore = document.getElementById('statTotalScore');
  const statPercentage = document.getElementById('statPercentage');
  const statCorrectCount = document.getElementById('statCorrectCount');
  const statIncorrectCount = document.getElementById('statIncorrectCount');
  const tryAgainBtn = document.getElementById('tryAgainBtn');
  const newQuizBtn = document.getElementById('newQuizBtn');

  // Review View
  const countAll = document.getElementById('countAll');
  const countCorrect = document.getElementById('countCorrect');
  const countIncorrect = document.getElementById('countIncorrect');
  const reviewItemsContainer = document.getElementById('reviewItemsContainer');
  const filterTabs = document.querySelectorAll('.filter-tab');

  // Modals & Extras
  const aiModal = document.getElementById('aiModal');
  const closeAiModalBtn = document.getElementById('closeAiModalBtn');
  const aiServerStatusText = document.getElementById('aiServerStatusText');
  const geminiApiKeyInput = document.getElementById('geminiApiKeyInput');
  const saveKeyBtn = document.getElementById('saveKeyBtn');
  const clearKeyBtn = document.getElementById('clearKeyBtn');
  const quitModal = document.getElementById('quitModal');
  const cancelQuitBtn = document.getElementById('cancelQuitBtn');
  const confirmQuitBtn = document.getElementById('confirmQuitBtn');
  const toastNotice = document.getElementById('toastNotice');
  const confettiCanvas = document.getElementById('confettiCanvas');

  // State
  let timerInterval = null;
  let elapsedSeconds = 0;
  let lastQuizConfig = null;
  let activeReviewData = [];
  let currentFilter = 'all';

  // -------------------------------------------------------------------------
  // Helper: Toast Notifications
  // -------------------------------------------------------------------------
  function showToast(message, duration = 3500) {
    if (!toastNotice) return;
    toastNotice.textContent = message;
    toastNotice.classList.add('show');
    setTimeout(() => {
      toastNotice.classList.remove('show');
    }, duration);
  }

  function formatLabel(str) {
    if (!str) return '';
    return str.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
  }

  // -------------------------------------------------------------------------
  // Helper: Screen Switcher
  // -------------------------------------------------------------------------
  function showScreen(screenElement) {
    [homeScreen, quizScreen, resultsScreen].forEach(screen => {
      screen.classList.remove('active-screen');
    });
    screenElement.classList.add('active-screen');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // -------------------------------------------------------------------------
  // Audio Control
  // -------------------------------------------------------------------------
  function updateSoundUI() {
    const isMuted = audio.isMuted();
    soundIcon.textContent = isMuted ? '🔇' : '🔊';
    soundToggleBtn.classList.toggle('active', !isMuted);
  }

  soundToggleBtn.addEventListener('click', () => {
    const muted = audio.toggleMute();
    updateSoundUI();
    showToast(muted ? 'Sound muted' : 'Sound enabled');
    if (!muted) audio.playClick();
  });
  updateSoundUI();

  // -------------------------------------------------------------------------
  // AI Settings Modal & Server Status Check
  // -------------------------------------------------------------------------
  async function updateAiServerStatusUI() {
    if (!aiServerStatusText) return;
    try {
      const status = await gemini.checkStatus();
      if (status.configured) {
        aiServerStatusText.innerHTML = `✅ <strong>Server Status:</strong> Gemini API key configured on server.`;
        aiServerStatusText.style.color = '#10B981';
        aiSettingsBtn.classList.add('active');
      } else {
        aiServerStatusText.innerHTML = `ℹ️ <strong>Server Status:</strong> No API key detected. Paste a key below or set <code>GEMINI_API_KEY</code> in <code>.env</code>.`;
        aiServerStatusText.style.color = 'var(--gold-300)';
      }
    } catch (e) {
      aiServerStatusText.innerHTML = `⚠️ <strong>Server Status:</strong> Could not connect to local server.`;
      aiServerStatusText.style.color = '#F59E0B';
    }
  }

  function openAiModal() {
    audio.playClick();
    updateAiServerStatusUI();
    aiModal.classList.add('open');
  }

  if (openAiModalBtn) {
    openAiModalBtn.addEventListener('click', openAiModal);
  }

  closeAiModalBtn.addEventListener('click', () => {
    audio.playClick();
    aiModal.classList.remove('open');
  });

  saveKeyBtn.addEventListener('click', async () => {
    audio.playClick();
    const key = geminiApiKeyInput.value.trim();
    saveKeyBtn.disabled = true;
    saveKeyBtn.textContent = 'Saving...';
    try {
      await gemini.setApiKey(key);
      await updateAiServerStatusUI();
      aiModal.classList.remove('open');
      showToast(key ? 'Gemini API Key saved securely to server!' : 'API Key cleared.');
    } catch (e) {
      showToast('Could not save key to server: ' + e.message);
    } finally {
      saveKeyBtn.disabled = false;
      saveKeyBtn.textContent = 'Save & Use AI Mode';
    }
  });

  clearKeyBtn.addEventListener('click', async () => {
    audio.playClick();
    await gemini.clearApiKey();
    geminiApiKeyInput.value = '';
    await updateAiServerStatusUI();
    aiModal.classList.remove('open');
    showToast('API key removed. Using verified local question bank.');
  });

  aiModal.addEventListener('click', (e) => {
    if (e.target === aiModal) {
      aiModal.classList.remove('open');
    }
  });

  // Check server status on initial page load
  gemini.checkStatus().then(updateAiServerStatusUI);

  // -------------------------------------------------------------------------
  // Timer Management
  // -------------------------------------------------------------------------
  function startTimer() {
    stopTimer();
    elapsedSeconds = 0;
    updateTimerDisplay();
    timerInterval = setInterval(() => {
      elapsedSeconds++;
      updateTimerDisplay();
    }, 1000);
  }

  function stopTimer() {
    if (timerInterval) {
      clearInterval(timerInterval);
      timerInterval = null;
    }
  }

  function updateTimerDisplay() {
    const mins = Math.floor(elapsedSeconds / 60);
    const secs = elapsedSeconds % 60;
    timerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }

  // -------------------------------------------------------------------------
  // Unified Quiz Generation Handler (Standard & AI Mode)
  // -------------------------------------------------------------------------
  async function handleStartQuiz(isAIMode = false) {
    audio.playClick();

    // Ensure we are viewing homeScreen before generating
    if (!homeScreen.classList.contains('active-screen')) {
      showScreen(homeScreen);
    }

    // Extract form parameters
    const formData = new FormData(quizSetupForm);
    const ageGroup = formData.get('ageGroup') || 'kids';
    const category = formData.get('category') || 'mixed';
    const difficulty = formData.get('difficulty') || 'medium';
    const questionCount = parseInt(formData.get('questionCount') || '10', 10);

    lastQuizConfig = { ageGroup, category, difficulty, questionCount, isAI: isAIMode };

    // Select which button triggered this action to show loading feedback
    const triggerBtn = isAIMode ? (aiGenerateBtn || aiSettingsBtn) : generateQuizBtn;
    const originalBtnHtml = triggerBtn.innerHTML;
    triggerBtn.disabled = true;
    triggerBtn.innerHTML = `
      <span style="display:inline-block;animation:spin 1s linear infinite;">⏳</span>
      <span>${isAIMode ? 'Generating AI Quiz...' : 'Generating Quiz...'}</span>
    `;

    try {
      let customQuestions = null;

      // Handle AI Mode question generation
      if (isAIMode) {
        showToast(`✨ Generating AI Quiz with Gemini: ${formatLabel(ageGroup)} • ${formatLabel(category)} • ${formatLabel(difficulty)}...`, 5000);
        try {
          customQuestions = await gemini.generateQuestions({
            ageGroup,
            category,
            difficulty,
            questionCount
          });
          showToast(`✨ AI Quiz Ready! Generated ${customQuestions.length} custom questions.`, 3000);
        } catch (aiErr) {
          console.warn('Gemini generation failed, falling back to local question bank:', aiErr);
          const isKeyError = aiErr.message && (aiErr.message.includes('API key') || aiErr.message.includes('API_KEY') || aiErr.message.includes('400'));
          if (isKeyError) {
            showToast(`⚠️ AI Mode: No Gemini API Key configured. Please enter your API key.`, 5000);
            openAiModal();
          } else {
            showToast(`⚠️ AI Mode notice: ${aiErr.message}. Falling back to verified local question bank.`, 5000);
          }
          // Seamless fallback to local question bank (Requirement 7)
          customQuestions = null;
          lastQuizConfig.isAI = false;
        }
      }

      // Initialize quiz through engine
      const quiz = engine.generateQuiz({
        ageGroup,
        category,
        difficulty,
        questionCount,
        customQuestions
      });

      if (!quiz.questions || quiz.questions.length === 0) {
        showToast('No questions found for selection. Please try again.');
        return;
      }

      // Update quiz header badges
      const ageLabels = {
        kids: 'Kids (6-10)',
        young_learners: 'Young Learners (11-15)',
        students: 'Students (16-20)',
        adults: 'Adults (21+)'
      };
      badgeAge.textContent = ageLabels[ageGroup] || ageGroup;
      badgeCategory.textContent = category === 'mixed' ? 'Mixed Categories' : category.charAt(0).toUpperCase() + category.slice(1);
      badgeDifficulty.textContent = difficulty.charAt(0).toUpperCase() + difficulty.slice(1);

      // AI Mode Badge visibility
      if (badgeAiMode) {
        badgeAiMode.style.display = quiz.isAI ? 'inline-flex' : 'none';
      }

      totalQNum.textContent = quiz.totalQuestions;

      // Render first question and display quiz screen
      renderCurrentQuestion();
      startTimer();
      showScreen(quizScreen);

    } catch (err) {
      console.error('Quiz creation error:', err);
      showToast('Error generating quiz. Please try again.');
    } finally {
      triggerBtn.disabled = false;
      triggerBtn.innerHTML = originalBtnHtml;
    }
  }

  // Standard Quiz Generation Button
  generateQuizBtn.addEventListener('click', () => handleStartQuiz(false));

  // AI Mode Button in Generator
  if (aiGenerateBtn) {
    aiGenerateBtn.addEventListener('click', () => handleStartQuiz(true));
  }

  // AI Mode Button in Header
  aiSettingsBtn.addEventListener('click', () => handleStartQuiz(true));

  // -------------------------------------------------------------------------
  // Render Current Question
  // -------------------------------------------------------------------------
  function renderCurrentQuestion() {
    const qState = engine.getCurrentQuestion();
    if (!qState) return;

    const { index, questionNumber, totalQuestions, questionData, userSelection } = qState;

    // Update Counter & Progress Bar
    currentQNum.textContent = questionNumber;
    const progressPercentValue = Math.round((questionNumber / totalQuestions) * 100);
    progressPercent.textContent = `${progressPercentValue}%`;
    progressBarFill.style.width = `${progressPercentValue}%`;

    // Category and Age tags
    questionCategoryTag.textContent = `Question ${questionNumber} • ${questionData.category.toUpperCase()}`;
    questionAgeTag.textContent = questionData.difficulty.toUpperCase();

    // Question Text
    activeQuestionText.textContent = questionData.question;

    // Render Options A, B, C, D
    const optionLetters = ['A', 'B', 'C', 'D'];
    optionsContainer.innerHTML = '';

    questionData.options.forEach((optText, optIdx) => {
      const optionLabel = document.createElement('label');
      optionLabel.className = 'option-item';

      const isChecked = userSelection && userSelection.selectedOptionIndex === optIdx;

      optionLabel.innerHTML = `
        <input type="radio" name="activeQuizOption" value="${optIdx}" ${isChecked ? 'checked' : ''}>
        <div class="option-content">
          <div class="option-letter">${optionLetters[optIdx]}</div>
          <div class="option-title">${escapeHtml(optText)}</div>
        </div>
      `;

      // Handle selection click
      const radioInput = optionLabel.querySelector('input');
      radioInput.addEventListener('change', () => {
        audio.playSelect();
        engine.recordAnswer(optIdx);
        updateNavigationButtons();
      });

      optionsContainer.appendChild(optionLabel);
    });

    updateNavigationButtons();
  }

  // -------------------------------------------------------------------------
  // Update Navigation Controls (Next / Prev / Finish)
  // -------------------------------------------------------------------------
  function updateNavigationButtons() {
    const qState = engine.getCurrentQuestion();
    if (!qState) return;

    const { index, totalQuestions, userSelection } = qState;

    // Previous Button
    prevQuestionBtn.disabled = (index === 0);

    // Next Button State: Must have selected an answer to proceed
    const hasAnswered = Boolean(userSelection && userSelection.selectedOptionIndex !== null);
    nextQuestionBtn.disabled = !hasAnswered;

    // Change Label on Last Question
    const isLast = engine.isLastQuestion();
    if (isLast) {
      nextBtnLabel.textContent = 'Finish Quiz & View Results';
      nextQuestionBtn.classList.add('btn-finish');
    } else {
      nextBtnLabel.textContent = 'Next Question';
      nextQuestionBtn.classList.remove('btn-finish');
    }
  }

  // Next / Finish Button Click
  nextQuestionBtn.addEventListener('click', () => {
    audio.playClick();
    if (engine.isLastQuestion()) {
      completeQuiz();
    } else {
      engine.nextQuestion();
      renderCurrentQuestion();
    }
  });

  // Prev Button Click
  prevQuestionBtn.addEventListener('click', () => {
    audio.playClick();
    engine.prevQuestion();
    renderCurrentQuestion();
  });

  // -------------------------------------------------------------------------
  // Complete Quiz & Render Results
  // -------------------------------------------------------------------------
  function completeQuiz() {
    stopTimer();
    const results = engine.finishQuiz();

    // Update Result Summary
    resultBadgeIcon.textContent = results.rankBadge;
    resultTitle.textContent = results.rankTitle;
    resultSubtitle.textContent = results.rankSubtitle;
    statTotalScore.textContent = `${results.correct} / ${results.total}`;
    statPercentage.textContent = `${results.percentage}%`;
    statCorrectCount.textContent = results.correct;
    statIncorrectCount.textContent = results.incorrect;

    // Review counts
    countAll.textContent = results.total;
    countCorrect.textContent = results.correct;
    countIncorrect.textContent = results.incorrect;

    // Populate Review List
    activeReviewData = results.review;
    currentFilter = 'all';
    renderReviewList();

    // Play victory sound & celebratory confetti
    audio.playSuccess();
    runConfetti();

    showScreen(resultsScreen);
  }

  // -------------------------------------------------------------------------
  // Render Detailed Question Review
  // -------------------------------------------------------------------------
  function renderReviewList() {
    reviewItemsContainer.innerHTML = '';

    const filtered = activeReviewData.filter(item => {
      if (currentFilter === 'correct') return item.isCorrect;
      if (currentFilter === 'incorrect') return !item.isCorrect;
      return true;
    });

    if (filtered.length === 0) {
      reviewItemsContainer.innerHTML = `
        <div style="text-align:center;padding:2rem;color:var(--text-light-muted);">
          No questions matching this filter.
        </div>
      `;
      return;
    }

    filtered.forEach((item, idx) => {
      const reviewCard = document.createElement('div');
      reviewCard.className = `review-item ${item.isCorrect ? 'is-correct' : 'is-incorrect'}`;

      const statusTag = item.isCorrect 
        ? `<span class="review-status-tag correct">✓ Correct</span>`
        : `<span class="review-status-tag incorrect">✗ Incorrect</span>`;

      const userChoiceHtml = item.selectedOptionIndex !== null
        ? `<div class="review-answer-pill user-choice ${item.isCorrect ? '' : 'wrong'}">
             <span class="answer-label">Your Answer:</span>
             <strong>${escapeHtml(item.selectedOptionText)}</strong>
           </div>`
        : `<div class="review-answer-pill user-choice wrong">
             <span class="answer-label">Your Answer:</span>
             <em>Not Answered</em>
           </div>`;

      const correctChoiceHtml = `
        <div class="review-answer-pill correct-choice">
          <span class="answer-label">Correct Answer:</span>
          <strong>${escapeHtml(item.correctOptionText)}</strong>
        </div>
      `;

      reviewCard.innerHTML = `
        <div class="review-meta">
          <span class="review-q-num">Question #${activeReviewData.indexOf(item) + 1} • <span style="text-transform:capitalize;">${item.category}</span></span>
          ${statusTag}
        </div>
        <div class="review-question-text">${escapeHtml(item.questionText)}</div>
        <div class="review-answers-box">
          ${userChoiceHtml}
          ${correctChoiceHtml}
        </div>
        <div class="review-explanation">
          <span class="review-explanation-icon">🦚</span>
          <div>
            <strong>Epic Context & Lesson:</strong> ${escapeHtml(item.explanation)}
          </div>
        </div>
      `;

      reviewItemsContainer.appendChild(reviewCard);
    });
  }

  // Filter tabs click handlers
  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      audio.playClick();
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      currentFilter = tab.getAttribute('data-filter') || 'all';
      renderReviewList();
    });
  });

  // -------------------------------------------------------------------------
  // Try Again & New Quiz Buttons
  // -------------------------------------------------------------------------
  tryAgainBtn.addEventListener('click', () => {
    audio.playClick();
    if (lastQuizConfig) {
      // Re-trigger quiz generation with same configuration
      generateQuizBtn.click();
    } else {
      showScreen(homeScreen);
    }
  });

  newQuizBtn.addEventListener('click', () => {
    audio.playClick();
    showScreen(homeScreen);
  });

  brandHomeBtn.addEventListener('click', () => {
    audio.playClick();
    if (quizScreen.classList.contains('active-screen')) {
      quitModal.classList.add('open');
    } else {
      showScreen(homeScreen);
    }
  });

  // -------------------------------------------------------------------------
  // Quit Quiz Modal Confirmation
  // -------------------------------------------------------------------------
  quitQuizBtn.addEventListener('click', () => {
    audio.playClick();
    quitModal.classList.add('open');
  });

  cancelQuitBtn.addEventListener('click', () => {
    audio.playClick();
    quitModal.classList.remove('open');
  });

  confirmQuitBtn.addEventListener('click', () => {
    audio.playClick();
    stopTimer();
    quitModal.classList.remove('open');
    showScreen(homeScreen);
    showToast('Quiz session ended.');
  });

  quitModal.addEventListener('click', (e) => {
    if (e.target === quitModal) {
      quitModal.classList.remove('open');
    }
  });

  // -------------------------------------------------------------------------
  // Celebratory Confetti Animation
  // -------------------------------------------------------------------------
  function runConfetti() {
    if (!confettiCanvas) return;
    const ctx = confettiCanvas.getContext('2d');
    const width = confettiCanvas.width = window.innerWidth;
    const height = confettiCanvas.height = window.innerHeight;

    const colors = ['#D4AF37', '#FFE082', '#007791', '#05B292', '#FFFDF7', '#F3C64F'];
    const particles = [];
    const count = 90;

    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height - height,
        r: Math.random() * 6 + 4,
        d: Math.random() * count,
        color: colors[Math.floor(Math.random() * colors.length)],
        tilt: Math.random() * 10 - 10,
        tiltAngleIncremental: (Math.random() * 0.07) + 0.05,
        tiltAngle: 0
      });
    }

    let animationFrame;
    let start = Date.now();

    function draw() {
      ctx.clearRect(0, 0, width, height);

      particles.forEach(p => {
        p.tiltAngle += p.tiltAngleIncremental;
        p.y += (Math.cos(p.d) + 3 + p.r / 2) / 1.5;
        p.x += Math.sin(p.d);
        p.tilt = Math.sin(p.tiltAngle - (p.r / 2)) * 15;

        ctx.beginPath();
        ctx.lineWidth = p.r / 2;
        ctx.strokeStyle = p.color;
        ctx.moveTo(p.x + p.tilt + (p.r / 4), p.y);
        ctx.lineTo(p.x + p.tilt, p.y + p.tilt + (p.r / 4));
        ctx.stroke();
      });

      if (Date.now() - start < 4500) {
        animationFrame = requestAnimationFrame(draw);
      } else {
        ctx.clearRect(0, 0, width, height);
      }
    }

    draw();
  }

  // -------------------------------------------------------------------------
  // Utility: HTML Escaping for Security
  // -------------------------------------------------------------------------
  function escapeHtml(text) {
    if (typeof text !== 'string') return text;
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
});
