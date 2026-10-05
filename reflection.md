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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
