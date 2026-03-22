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
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This is a game application where you're supposed to guess the secret number and use the hints to get you closer to the correct answer.
- [ ] Detail which bugs you found.
1. There was a weird, broken link next to "Make a Guess"
2. The logic of the hints were swapped.
3. For every 2nd attempt you did, your answer would be converted to a string instead of staying as a number
4. The ranges for the various game modes were wrong (ex. hard had a more smaller range whereas medium had a wider range)
5. No penalizing for wrong guesses
- [ ] Explain what fixes you applied.
1. Fixed the logic of the hints in check_guess
2. removed the str() conversion in app.py

## 📸 Demo

![Game screenshot](Screenshot 2026-03-22 at 12.03.01 PM.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
