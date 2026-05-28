import random

words = ["python", "apple", "coding", "computer", "developer"]

chosen_word = random.choice(words)

display = []

for letter in chosen_word:
    display += "_"

lives = 6

print("Welcome to Hangman")

game_over = False

while not game_over:

    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("Wrong Guess")
        print("Lives left:", lives)

        if lives == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You Win")