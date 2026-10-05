# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

## Response:
The game at the beginning was very glitchy, the "New Game" button kept on displaying an error message that was too immediate to be seen, and some buttons had to be clicked multiple times for them to take effect. The hints were quite wrong and the logic of the difficulty levels didn't make sense. 
Two concrete bugs I immediately noticed were:
- no restriction about the range; it would say that the range was 1-100 but allow any number (like 200) to be inputed
- the "new game" button didn't work properly, there was no way to start a new game

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior  | Actual Behavior | Console Output / Error |
|-------|------------------- |-----------------|------------------------|
|"hello"| TypeError          | did not specify | "hello" marked in      |
                              that there was      history
                              any error with 
                              the string input

| 27    | "Correct!"         | "Go higher!"    |   Secret number: 27    |
                                                  Secret number: 35

| 4.5   | "Enter an integer" | "Go lower!"     |  4.5 marked in history |
| Click | Empty input box    | 46 (from last   |  46 still in input box |
  New                               game)
  Game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

## Response:
For this project I used Copilot built into VSCode. 

One AI suggestion that was correct that I hadn't caught at first was that the game sometimes passes {secret} as a string, so comparing them in the Try: TypeError block would raise an error. Copilot suggested keeping both values numeric, so avoiding the conversion of {secret} to a string was the best solution for this. I first asked Copilot to identify any errors in the logic and once I read through its suggestion and understood what needed to be fixed, I asked the AI to fix that logic. 

One AI suggestion I did not take as written was with the function {update_score}. The AI made changes that I didn't understand much at first since it compressed a long block of code into a much shorter version. I asked the AI to explain the logic behind what it had suggested and why these changes to the function were necessary. It explained its suggestions which involved correcting the winning score calculation (previously, users who got the number correct on the first attempt did not get a full 100 points score) and making incorrect guesses consistent (the previous logic deducted a different amount of points for the guess being "too low" versus "too high" -- logically it would make sense for ANY incorrect answer to deduct the same number of points). Once I understood the reasons for the changes and verified them, I accepted the AI's code because I didn't find anything that was wrong with it or that could be better optimized.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

## Response:
I decided whether a bug was really fixed once I understood well what the changes to the code had been (and if they were absolutely necessary) and then tested it myself on the game page with various different scenarios based on the developer tools. 
One test I ran using pytest was to verify how well check_guess worked. The test the same function with 6 different input cases to test against the different options that a user might enter during the game and how the program would respond back. The test verifies that the program accurately returns back the appropriate responses such as "Too high!" or "Too low!" based on user input. I also verified the performance of this feature manually by testing it out on the gamepage with my own inputs to see how the game reacted. 
AI only helped me design and understand the pytest written for check_guess and what the different input cases were checking for.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

## Response:
Streamlit is a sort of model that basically "refreshes" the page and runs the program's code from the first line again each time that you interact with the page in any way. Streamlit is really helpful when you want to create page interfaces using only Python, which saves you from having to create additional files or write more code in other languages to make the visuals. At the same time, because Streamlit "refreshes" each time, it's almost as if it resets the data that you input into the page, so for example if you type a number into a box, Streamlit would probably reset that box to a default value and not keep the number you entered. But that's where session state comes in-- it allows Streamlit to keep track of that data that you input, even when the program "reruns" the code behind the scenes. That way, it can keep using that data as long as it's relevant to the program. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

## Response: 
One habit that I want to reuse in future projects is verifying well what the AI suggests and the code that it gives me. I try to be wary of AI code because I know that it can often make mistakes or misinterprets what I have in mind, but sometimes when the code is too complicated, I tend to simply trust that the AI knows what it's doing and take the code as it is-- I will make sure to be more conscious of what code I'm using from the AI. 
I think something that would have been beneficial for this project is asking the AI to explain to me at the beginning what the current code was doing. Not identify mistakes or fix them, but simply how the starting logic worked, and from there I could have gotten a better sense of what logic might be faulty. I will do this next time I work with AI on a coding task.
I think the AI's code worked well in this project, but I think in order for it to work well, you have to be specific about what you want the AI to do. For that, you need to understand the code first, so I'd say AI isn't a substitution for learning to code, but more so a tool to help guide you in the process while being consistently steered in the right direction. 

