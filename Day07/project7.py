# Project7

import random

ascii = [
'''  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]
print("----------------------------------------------------------")
print("WELCOME TO THE CLASSIC HANDMAN GAME!")
print("----------------------------------------------------------")
print("Guess the correct letters of the unknown word or you might just get HANGED.")

word_list = ["apple", "window", "college", "chair", "books"]
chosen_word = random.choice(word_list)

display = "_" * len(chosen_word)
wrong_guesses = 0
max_wrong = 6

print(display)
print(ascii[wrong_guesses])

game_over = False

while not game_over:
    guess = input("Enter a letter: ").lower()

    new_display = ""
    correct_guess = False

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            new_display += guess
            correct_guess = True
        else:
            new_display += display[i]

    display = new_display
    print(display)

    if not correct_guess:
        wrong_guesses += 1
        print(f"Wrong guess! Attempts left: {max_wrong - wrong_guesses}")
    else:
        print("Correct guess!")

    print(ascii[wrong_guesses])

    if "_" not in display:
        print("You win!")
        game_over = True

    if wrong_guesses == max_wrong:
        print("You lose!")
        game_over = True
