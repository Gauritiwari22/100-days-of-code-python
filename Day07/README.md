# Project 7 – Hangman Game (Python)

## Description
This project is a console-based implementation of the classic **Hangman** game using Python.  
The program randomly selects a word, and the player must guess it letter by letter before the hangman is fully drawn.

With each wrong guess, a new part of the hangman is added using ASCII art.

---

## How the Game Works
- A random word is chosen from a predefined list.
- The player guesses one letter at a time.
- Correct guesses reveal the letter in the word.
- Wrong guesses add parts to the hangman drawing.
- The game ends when:
  - the word is completely guessed (**win**), or
  - the hangman is fully drawn (**lose**).

---

## Concepts Used
- Python loops (`while`, `for`)
- Conditional statements
- Strings and string immutability
- State management using variables
- ASCII art representation
- Random module

---

## Key Logic
- The game starts with an empty hangman pole.
- Each incorrect guess increments the count of wrong guesses.
- ASCII art is displayed based on the number of wrong guesses.
- The current progress of the word is preserved across guesses.

---





