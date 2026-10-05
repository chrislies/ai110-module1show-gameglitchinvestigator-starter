# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- When starting the app for the first time Attempts is set to 1 even though no guess has been made.
- The hint is inverted: guessing a number that is lower than the answer will tell you to go lower and vice versa.
- Guessing the answer correct on the first try produces a final score of 70. Not sure if this is a bug or intended.
- Starting a new game creates a new secret answer but does not allow guesses to be submitted.
- The history stack is delayed. A guess gets appended onto the stack after you make a subsequent guess.

**Bug Reproduction Log**
| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| - | - | - | - |
| Submitting a guess lower than the answer | Hint should say guess higher | Hint says guess lower | n/a |
| Number of attempts is set to 1 at the beginning of each game | Number of attempts should be reset to 0 when new game starts | Number of attempts is set to 1 after resetting | n/a |
| Starting a new game does not allow guesses to be submitted | Game should allow new guesses for a new game | Game does not allow new guesses after game is reset | n/a |
| History stack is delayed | Submitting a guess should be reflected on the history stack | A guess is appended to the history stack after a subsequent guess is made | n/a |

---

## 2. How did you use AI as a teammate?

I used Claude Code to help guide my process in addressing issues in the code and explaining why certain features did not work as intended. One correct suggestion Claude Code made was to swap the the lower/higher hint messages since it would previously recommend to guess higher when submitting a guess that is higher than the answer and vice versa. One suggestion Claude Code made I did not accept was regarding the bug that prevented new guesses from being submitted after restarting a new game. The proposed solution did not take into consideration that all session states had to be reset which was something I had to emphasize.

---

## 3. Debugging and testing your fixes

A bug is considered fix if it passes all possible pytest test cases. I asked Claude Code to generate comprehensive tests for each of the game logic functions and to explain what each tests checks for. Having a large parameter set for the tests allow for multiple test cases to be checked.

---

## 4. What did you learn about Streamlit and state?

The script runs top to bottom and re-runs the entire script whenever you interact with anything (clicking a button, submitting an entry, etc). Consequently, any variables set in the script will also be reset. This is why session state is crucial in Streamlit apps as the state does not get reset between app re-runs. The session state lives as long as your browser's tab/session stays open. Therefore, you should use session state for anything you want the app to remember.

---

## 5. Looking ahead: your developer habits

One habit/strategy I want to use in future projects is to use AI to help create tests for my logic functions as I create them. Somethign I would do differently next time I work with AI on a coding task is to start small; understand what each function does and then build upon it or refactor for better efficiency and management. This project showed me how to efficiently use AI to guide me in finding and addressing bugs, and how to create comprehensive test cases in pytest to ensure functions are working as intended.
