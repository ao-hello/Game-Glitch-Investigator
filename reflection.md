# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The user interface and the "interactness" of the entire game is fine, it's just that the hints are far off; for example, if it tells you to go lower based on your guess, for your next hint, it would probably tell you to go higher if you enter a lower number than your previous guess. And sometimes, the hints may imply that the target number is outside the accepted range. 
- List at least two concrete bugs you noticed at the start   
  (for example: "the secret number kept changing" or "the hints were backwards").
The first bug i noticed was the broken link next to the "Make a guess" text. The link didn't take you anywhere. The other bug was how misleading the hints were. Like I said before, for example, if the hint told you to go lower based on what you put as your previous answer and you actually put a lower number, the next hint would probably tell you to go higher as a result.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I ended up using Claude. I am the most familiar with Claude. I also don't have any experiences with the other AI tools, besides Copilot. I am not quite fond of Copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One suggestion that was right was the logic error in the check_guess function. When first given the starter code, I skimmed through everything and didn't really look much into the code in detail. When the AI told me about the function's logic, I decided to look over it myself and ended determining that the AI was correct to point out this glitch to me. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I'm not quite if this could be counted as incorrect or misleading but, Claude suggested that the tests in the test_game_logic were bugs as well. Its reasoning was something along the lines of the tests returning a tuple even though they were being compared against plain strings. I essentially told claude not to be nitpicking and focus on the errors that truly matter.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided whether a bug was really fixed by afterwards, opening up the game and playing it myself. Actually playing and interacting with the game made it easier for me to understand whether or not the game still didn't make any sense or if did. This was the method I commonly used.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a test using pytest. The results from the pytest confirmed that the bugs previously found in the starter code have now been resolved. It shows that now, the important core logic is correctly implemented. 
- Did AI help you design or understand any tests? How?
Yes; as I use a macbook, it showed me the correct commands I should do to actually run the pytest. At first, not all the test were passing, and Claude reminded me again that, appearently, some of the tests in test_game_logic were implenmented incorrectly, and so, it helped me fix that. In regards to reading and understanding the pytests, I had no problem figuring that all on my own.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Everytime you clicked a button in the game application, it would cause the entire code to run all over again, With random.randint() being at the top of the file, that meant that a new target number was created with every interaction/click. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Think of Streamlit as a website or webpage and the reruns as reloading that webpage. Everytime you reload though, your progress doesn't save; you get a fresh, clean start everytime. The session_state or "state", however, is the bits of memory from a previous "webpage" that you wish to carry on across all reloads.  
- What change did you make that finally gave the game a stable secret number?
A conditional statement was added to app.py:93-94. This if statement checks if there isn't already a secret number generated. If there isn't one, a new secret number will be generated. Otherwise, the conditional will fail, perserving the same secret number across all sessions. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One thing I will takeaway from this activity is ensuring that the AI agent has all relevent context from the project files. I made sure the agent I used, Claude, knew what was going on, the purpose of the game application, and what I needed help with. 
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I'll do differently next time is thoroughly look over/study the code before handing it off to the AI. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
For the most part, AI generated code can be good enough to solve simple topics or problems. But I think it's good practice to create your own code first, and then use AI for suggestions on how to make your already existing code efficient, more simpler, etc.