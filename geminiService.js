/**
 * Gemini AI Question Generator Service
 * 
 * Securely communicates with the backend API gateway without exposing
 * any Gemini API keys in frontend JavaScript.
 * Automatically falls back to the verified local question bank if the server
 * or AI generation encounters any error.
 */

class GeminiService {
  constructor() {
    this.apiEndpoint = '/api/generate-questions';
    this.statusEndpoint = '/api/ai-status';
    this.setKeyEndpoint = '/api/set-key';
    this.isConfiguredOnServer = false;
    this.sessionKey = '';
  }

  /**
   * Checks with server whether an API key is configured in the environment or .env
   */
  async checkStatus() {
    try {
      const response = await fetch(this.statusEndpoint, { method: 'GET' });
      if (response.ok) {
        const data = await response.json();
        this.isConfiguredOnServer = Boolean(data.configured);
        return data;
      }
    } catch (e) {
      // Server not reachable
    }
    return { configured: false };
  }

  /**
   * Determines if AI Mode is ready (either via server env or session key)
   */
  hasApiKey() {
    return this.isConfiguredOnServer || Boolean(this.sessionKey && this.sessionKey.length > 5);
  }

  /**
   * Sets or updates API key securely via backend endpoint
   */
  async setApiKey(key) {
    this.sessionKey = (key || '').trim();
    try {
      const response = await fetch(this.setKeyEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ apiKey: this.sessionKey })
      });
      if (response.ok) {
        const data = await response.json();
        this.isConfiguredOnServer = Boolean(data.configured);
        return data;
      }
    } catch (e) {
      console.warn('Could not persist key to server endpoint:', e);
    }
    this.isConfiguredOnServer = Boolean(this.sessionKey && this.sessionKey.length > 5);
    return { success: true };
  }

  /**
   * Clears API key from session and server
   */
  async clearApiKey() {
    this.sessionKey = '';
    this.isConfiguredOnServer = false;
    try {
      await fetch(this.setKeyEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ apiKey: '' })
      });
    } catch (e) {}
  }

  /**
   * Generates dynamic Mahabharata questions tailored specifically to selections
   * @param {Object} params - { ageGroup, category, difficulty, questionCount }
   * @returns {Promise<Array>} Array of validated question objects
   */
  async generateQuestions({ ageGroup, category, difficulty, questionCount = 10 }) {
    const headers = {
      'Content-Type': 'application/json'
    };
    if (this.sessionKey) {
      headers['X-Gemini-Key'] = this.sessionKey;
    }

    let response;
    try {
      response = await fetch(this.apiEndpoint, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify({
          ageGroup,
          category,
          difficulty,
          questionCount: parseInt(questionCount, 10) || 10,
          apiKey: this.sessionKey || undefined
        })
      });
    } catch (netErr) {
      throw new Error(`Cannot reach local AI server. Please make sure 'python run_server.py' is running. (${netErr.message})`);
    }

    const data = await response.json().catch(() => ({}));

    if (!response.ok || !data.success) {
      const errMsg = data.error || `Server responded with status ${response.status}`;
      throw new Error(errMsg);
    }

    if (!Array.isArray(data.questions) || data.questions.length === 0) {
      throw new Error('AI returned an empty question set. Falling back to local bank.');
    }

    // Validate structure of each question
    const validated = data.questions.map((q, idx) => ({
      id: q.id || `ai_${Date.now()}_${idx}`,
      question: q.question,
      options: Array.isArray(q.options) && q.options.length === 4 ? q.options : ['A', 'B', 'C', 'D'],
      answer: typeof q.answer === 'number' && q.answer >= 0 && q.answer <= 3 ? q.answer : 0,
      explanation: q.explanation || 'Educational context from the epic.',
      category: q.category || category,
      difficulty: q.difficulty || difficulty,
      ageGroup: q.ageGroup || ageGroup,
      isAI: true
    }));

    return validated;
  }
}

if (typeof window !== 'undefined') {
  window.geminiService = new GeminiService();
}
