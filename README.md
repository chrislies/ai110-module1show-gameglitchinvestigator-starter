# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The purpose of this game is to guess a secret number. If your guess is too low or too high the game will recommend you to guess higher or lower respectively. The game concludes when you either guess correctly or when you run out of allowed guesses.
- Some bugs I found include the following:
  - When starting the app for the first time Attempts is set to 1 even though no guess has been made.
  - The hint is inverted: guessing a number that is lower than the answer will tell you to go lower and vice versa.
  - Starting a new game creates a new secret answer but does not allow guesses to be submitted.
  - The history stack is delayed. A guess gets appended onto the stack after you make a subsequent guess.
- To address these issues I did the following (with guidance from Claude Code):
  - Initialize the Attempt session state to 0.
  - Swap the messages for the lower/higher hints
  - Reset session state for attempts, secret, status, history, and score when starting a new game to ensure a fresh start.
  - Render attempts/debug info into placeholders so they can be filled after the submit is processed, keeping them in sync with the latest guess

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 20
2. Game returns "Too High"
3. User enters a guess of 10
4. Game returns "Too Low"
5. Score updates correctly after each guess
6. Game ends after the correct guess

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\cl4282\Programming\codepath\ai110\module1\ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
plugins: anyio-4.15.1
collected 53 items

tests\test_game_logic.py .....................................................                                                                                   [100%]

========================================================================= 53 passed in 0.25s ==========================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
