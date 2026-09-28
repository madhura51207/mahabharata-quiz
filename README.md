# 🦚 Mahabharata Quiz

An interactive, modern educational web application designed to test and enrich understanding of the ancient Indian epic **The Mahabharata** across different age groups.

---

## 🌟 Key Features

1. **Age-Appropriate Learning**:
   - **Kids (6–10)**: Focuses on legendary heroes (Arjuna, Krishna, Bhima), simple archery tests, valor, animals, and inspiring friendship.
   - **Young Learners (11–15)**: Covers Kurukshetra events, divine astras, the dice match, exile, and heroic battles.
   - **Students (16–20)**: Delves into strategy, characters' moral dilemmas, and the timeless philosophy of the *Bhagavad Gita*.
   - **Adults (21+)**: Explores the deeper nuances of Dharma, specific Parvas, genealogy, ethical conflicts, and *Vidura Niti*.

2. **Categorized Exploration**:
   - 👑 **Characters** (Arjuna, Krishna, Bhishma, Karna, Draupadi, etc.)
   - 📖 **Stories & Events** (The game of dice, Lakshagriha, Chakravyuha, Kurukshetra war)
   - ⚔️ **Weapons & Astras** (Gandiva, Sudarshana Chakra, Pashupatastra, Narayanastra)
   - 🏰 **Places** (Hastinapura, Indraprastha, Dwaraka, Kurukshetra, Matsya Kingdom)
   - 🤝 **Relationships** (Lineage, fraternal bonds, vows, and rivalries)
   - ⚖️ **Values & Lessons** (*Satya*, *Dharma*, focus, selfless duty / *Nishkama Karma*)
   - ✨ **Mixed** (Blended selection across all categories)

3. **Customizable Quiz Experience**:
   - Select difficulty: **Easy**, **Medium**, or **Hard**.
   - Select quiz length: **5**, **10**, or **20** questions.
   - Intelligent fallback and question blending: ensures the exact requested number of questions is always delivered with zero duplicates.

4. **Interactive Quiz Interface**:
   - Shows **one question at a time**.
   - Live question counter (`Question 3 of 10`) and animated progress bar.
   - Real-time session timer.
   - 4 clearly labeled multiple-choice options (`A`, `B`, `C`, `D`) with instant selection feedback.
   - Built-in sound effects generated via native Web Audio API (zero audio downloads, toggleable on/off).
   - "Previous" and "Next" navigation controls to allow reviewing before final submission.

5. **Detailed Results & Performance Review**:
   - Total score, accuracy percentage, correct answers count, and incorrect answers count.
   - Age-tailored heroic persona titles (e.g. *Supreme Maharatha*, *Arjuna's Sharpshooter Vision*, *Valiant Dharmic Yoddha*).
   - Full question-by-question review:
     - Clear comparison between your choice and the correct answer.
     - Informative educational explanation providing historical context and moral lessons.
     - Review filter tabs: **All**, **Correct**, and **Incorrect**.
   - **Try Again** button to instantly take another randomized quiz with the same settings.
   - **Change Settings** button to explore different age groups and categories.

6. **Regal Visual Design**:
   - Color palette: **Dark Royal Navy** (`#0B132B`, `#121C38`), **Warm Gold** (`#D4AF37`, `#F3C64F`), and **Ancient Cream/Parchment** (`#FDFBF7`, `#F9F5EC`).
   - Clean, modern layout avoiding visual clutter.
   - Subtle Mahabharata motifs: *Dharmachakra* chariot wheel, peacock feather emblem, and *Gandiva* bow iconography.
   - Fully responsive for mobile, tablet, and desktop screens.

7. **Zero-API Offline First + Optional AI Generation**:
   - Comes out of the box with a rich **120+ Curated Question Bank** that works **100% offline** without any setup or API keys.
   - Cleanly separated optional **Gemini AI service** (`geminiService.js`) with an in-app settings modal for users who wish to generate brand new dynamic AI questions.

---

## 📁 Project Architecture

```
ADM_PROJECT/
├── index.html                 # Main web application entry point
├── css/
│   ├── style.css              # Global styles, variables, typography, layouts, animations
│   └── components.css         # UI cards, options, progress bar, badges, review list, modals
├── js/
│   ├── data/
│   │   └── questions.js       # Curated 120+ Mahabharata questions with explanations
│   ├── quizEngine.js          # Core quiz generation, randomization, scoring, and state
│   ├── geminiService.js       # Optional dynamic AI generation via Gemini API (separated)
│   ├── audioService.js        # Built-in sound effects using Web Audio API (100% offline)
│   └── app.js                 # UI coordination, event listeners, view switches, confetti
├── assets/
│   ├── favicon.svg            # Custom themed bow and wheel favicon
│   ├── peacock.svg            # Stylized Krishna peacock feather motif
│   ├── chariot-wheel.svg      # Dharmachakra / Kurukshetra chariot wheel motif
│   └── bow-arrow.svg          # Arjuna's Gandiva bow & arrow SVG icon
├── tests/
│   ├── test_bank.py           # Validates question structure, options, answers, and coverage
│   └── test_engine_simulation.py # Validates all 252 permutation combinations of settings
├── run_server.py              # Lightweight Python local HTTP server runner
├── start_quiz.bat             # One-click Windows launch script
└── README.md                  # Project documentation
```

---

## 🚀 How to Run the Website

### Option 1: Direct File Opening
Simply double-click [`index.html`](file:///c:/Users/madhu/Downloads/ADM_PROJECT/index.html) in your file manager to open it in any modern web browser (Chrome, Edge, Firefox, Safari).

### Option 2: Using the Python Server (Recommended)
Run the included Python server runner:
```bash
python run_server.py
```
This will launch the local HTTP server at `http://localhost:8000` and automatically open your default web browser.

### Option 3: Windows Batch Script
On Windows, simply double-click [`start_quiz.bat`](file:///c:/Users/madhu/Downloads/ADM_PROJECT/start_quiz.bat).

---

## 🧪 Testing and Verification

To verify the question bank and quiz engine logic across all 252 permutations:

```bash
# Verify integrity of all 120 questions
python tests/test_bank.py

# Verify quiz generation engine across all combinations
python tests/test_engine_simulation.py
```

---

## 📜 Educational Value & Philosophy

> *“यतो धर्मस्ततो जयः”*  
> *(Yato Dharmastato Jayah — Where there is Dharma, there is Victory)*

This application is built not merely as a test of memory, but as a journey of reflection into ancient Indian philosophy, ethical decision-making, and the timeless pursuit of righteousness.
