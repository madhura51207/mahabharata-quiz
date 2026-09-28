/**
 * Mahabharata Quiz - Core Quiz Engine
 * Handles question filtering, intelligent fallback blending, option shuffling,
 * state management, timer calculation, scoring and performance evaluation.
 * Separated cleanly from the UI presentation layer.
 */

class QuizEngine {
  constructor(questionBank) {
    this.questionBank = Array.isArray(questionBank) ? questionBank : [];
    this.currentQuiz = null;
    this.currentIndex = 0;
    this.userAnswers = [];
    this.startTime = null;
    this.endTime = null;
    this.timerInterval = null;
    this.elapsedSeconds = 0;
  }

  /**
   * Shuffles an array in place with Fisher-Yates algorithm
   */
  static shuffleArray(array) {
    const copy = [...array];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  /**
   * Generates a customized quiz based on user criteria.
   * If a specific filter contains fewer questions than requested, it gracefully
   * expands search to ensure the requested count is ALWAYS satisfied without duplicates.
   */
  generateQuiz({ ageGroup, category, difficulty, questionCount = 10, customQuestions = null }) {
    const requestedCount = parseInt(questionCount, 10) || 10;
    const selectedCategory = category ? category.toLowerCase() : 'mixed';
    const selectedAge = ageGroup ? ageGroup.toLowerCase() : 'young_learners';
    const selectedDifficulty = difficulty ? difficulty.toLowerCase() : 'medium';

    let candidates = [];
    const usedIds = new Set();

    // If customQuestions (e.g. from AI generation) are provided, use them first
    if (Array.isArray(customQuestions) && customQuestions.length > 0) {
      for (const q of customQuestions) {
        if (candidates.length < requestedCount && !usedIds.has(q.id)) {
          candidates.push(q);
          usedIds.add(q.id);
        }
      }
    }

    // If more questions are needed (or no customQuestions), fill from questionBank
    if (candidates.length < requestedCount) {
      const pool = this.questionBank;
      const addCandidates = (filterFn) => {
        const matches = pool.filter(q => !usedIds.has(q.id) && filterFn(q));
        const shuffledMatches = QuizEngine.shuffleArray(matches);
        for (const q of shuffledMatches) {
          if (candidates.length < requestedCount) {
            candidates.push(q);
            usedIds.add(q.id);
          }
        }
      };

      // Stage 1: Exact matches (ageGroup + category + difficulty)
      addCandidates(q => {
        const ageMatch = q.ageGroup === selectedAge;
        const catMatch = selectedCategory === 'mixed' || q.category === selectedCategory;
        const diffMatch = q.difficulty === selectedDifficulty;
        return ageMatch && catMatch && diffMatch;
      });

      // Stage 2: Same ageGroup + category, any difficulty
      if (candidates.length < requestedCount) {
        addCandidates(q => {
          const ageMatch = q.ageGroup === selectedAge;
          const catMatch = selectedCategory === 'mixed' || q.category === selectedCategory;
          return ageMatch && catMatch;
        });
      }

      // Stage 3: Same ageGroup, any category, any difficulty
      if (candidates.length < requestedCount) {
        addCandidates(q => q.ageGroup === selectedAge);
      }

      // Stage 4: Same category across adjacent age groups
      if (candidates.length < requestedCount) {
        addCandidates(q => selectedCategory === 'mixed' || q.category === selectedCategory);
      }

      // Stage 5: Fallback to any remaining questions in pool
      if (candidates.length < requestedCount) {
        addCandidates(() => true);
      }
    }

    // Only shuffle candidate question order if not AI
    if (!customQuestions) {
      candidates = QuizEngine.shuffleArray(candidates);
    }

    // Deep clone and shuffle options for each question so correct answer is tracked properly
    this.currentQuiz = candidates.map((q, idx) => {
      const originalOptions = [...q.options];
      const correctText = originalOptions[q.answer];

      // Shuffle options
      const shuffledOptions = QuizEngine.shuffleArray(originalOptions);
      const newAnswerIndex = shuffledOptions.indexOf(correctText);

      return {
        id: q.id || `q_${idx}`,
        originalId: q.id,
        question: q.question,
        options: shuffledOptions,
        answer: newAnswerIndex,
        correctAnswerText: correctText,
        explanation: q.explanation || 'No explanation provided.',
        category: q.category,
        difficulty: q.difficulty,
        ageGroup: q.ageGroup,
        isAI: Boolean(q.isAI)
      };
    });

    this.currentIndex = 0;
    this.userAnswers = new Array(this.currentQuiz.length).fill(null);
    this.startTime = Date.now();
    this.endTime = null;
    this.elapsedSeconds = 0;

    return {
      totalQuestions: this.currentQuiz.length,
      questions: this.currentQuiz,
      isAI: this.currentQuiz.some(q => q.isAI)
    };
  }

  getCurrentQuestion() {
    if (!this.currentQuiz || this.currentIndex < 0 || this.currentIndex >= this.currentQuiz.length) {
      return null;
    }
    return {
      index: this.currentIndex,
      questionNumber: this.currentIndex + 1,
      totalQuestions: this.currentQuiz.length,
      questionData: this.currentQuiz[this.currentIndex],
      userSelection: this.userAnswers[this.currentIndex]
    };
  }

  recordAnswer(optionIndex) {
    if (!this.currentQuiz || this.currentIndex >= this.currentQuiz.length) return;

    const currentQ = this.currentQuiz[this.currentIndex];
    const isCorrect = optionIndex === currentQ.answer;

    this.userAnswers[this.currentIndex] = {
      questionId: currentQ.id,
      selectedOptionIndex: optionIndex,
      selectedOptionText: optionIndex !== null ? currentQ.options[optionIndex] : null,
      correctOptionIndex: currentQ.answer,
      correctOptionText: currentQ.correctAnswerText,
      isCorrect: isCorrect,
      explanation: currentQ.explanation,
      questionText: currentQ.question,
      options: currentQ.options,
      category: currentQ.category,
      difficulty: currentQ.difficulty
    };

    return this.userAnswers[this.currentIndex];
  }

  nextQuestion() {
    if (this.currentIndex < this.currentQuiz.length - 1) {
      this.currentIndex++;
      return true;
    }
    return false;
  }

  prevQuestion() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      return true;
    }
    return false;
  }

  jumpToQuestion(index) {
    if (index >= 0 && index < this.currentQuiz.length) {
      this.currentIndex = index;
      return true;
    }
    return false;
  }

  isLastQuestion() {
    return this.currentIndex === (this.currentQuiz ? this.currentQuiz.length - 1 : 0);
  }

  isAllAnswered() {
    return this.userAnswers.every(ans => ans !== null && ans.selectedOptionIndex !== null);
  }

  finishQuiz() {
    this.endTime = Date.now();
    const durationMs = this.endTime - (this.startTime || this.endTime);
    this.elapsedSeconds = Math.round(durationMs / 1000);

    const total = this.currentQuiz.length;
    let correct = 0;
    let incorrect = 0;
    let unanswered = 0;

    for (let i = 0; i < total; i++) {
      const record = this.userAnswers[i];
      if (!record || record.selectedOptionIndex === null) {
        unanswered++;
        // Auto populate unanswered record for review
        if (!record) {
          const q = this.currentQuiz[i];
          this.userAnswers[i] = {
            questionId: q.id,
            selectedOptionIndex: null,
            selectedOptionText: 'Not Answered',
            correctOptionIndex: q.answer,
            correctOptionText: q.correctAnswerText,
            isCorrect: false,
            explanation: q.explanation,
            questionText: q.question,
            options: q.options,
            category: q.category,
            difficulty: q.difficulty
          };
        }
      } else if (record.isCorrect) {
        correct++;
      } else {
        incorrect++;
      }
    }

    const percentage = total > 0 ? Math.round((correct / total) * 100) : 0;
    const evaluation = QuizEngine.getEvaluation(percentage);

    return {
      total,
      correct,
      incorrect,
      unanswered,
      percentage,
      elapsedSeconds: this.elapsedSeconds,
      formattedTime: QuizEngine.formatTime(this.elapsedSeconds),
      rankTitle: evaluation.title,
      rankSubtitle: evaluation.subtitle,
      rankBadge: evaluation.badge,
      review: this.userAnswers
    };
  }

  static getEvaluation(percentage) {
    if (percentage === 100) {
      return {
        title: "Supreme Maharatha",
        subtitle: "Incredible mastery! Like Veda Vyasa's supreme scholar, your knowledge of Dharma and the epic is flawless.",
        badge: "👑"
      };
    } else if (percentage >= 80) {
      return {
        title: "Arjuna's Sharpshooter Vision",
        subtitle: "Outstanding performance! Your focus and depth of understanding pierce through the hardest questions.",
        badge: "🏹"
      };
    } else if (percentage >= 60) {
      return {
        title: "Valiant Dharmic Yoddha",
        subtitle: "Great knowledge! You have a solid grasp of the great saga and its timeless teachings.",
        badge: "🛡️"
      };
    } else if (percentage >= 40) {
      return {
        title: "Aspiring Seeker of Wisdom",
        subtitle: "A promising effort! Review the explanations below to unlock deeper secrets of the Mahabharata.",
        badge: "📜"
      };
    } else {
      return {
        title: "Novice Explorer of the Epic",
        subtitle: "Every great hero begins as a student. Read through the review below and try again to sharpen your skills!",
        badge: "✨"
      };
    }
  }

  static formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }
}

// Export for module/browser global
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { QuizEngine };
} else if (typeof window !== 'undefined') {
  window.QuizEngine = QuizEngine;
}
