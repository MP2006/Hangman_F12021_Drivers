import random

import format

stages = format.stages
word_list = ["verstappen", "hamilton", "bottas", "perez", "sainz", "norris", "leclerc", "ricciardo", "gasly", "alonso",
             "ocon", "vettel", "stroll", "tsunoda", "russell", "raikkonen", "latifi",
             "giovinazzi", "schumacher", "mazepin", "kubica"]
choice = "y"
while choice == "y":
    lives = 6
    selectWord = random.choice(word_list)
    lengthWord = len(selectWord)

    print("\nWelcome to Hangman!\nF1 2021 Drivers Edition\n")

    listWord = []
    y = 0
    for x in range(lengthWord):
        listWord.append("_")

    while "_" in listWord and lives != 0:
        playing = " ".join(listWord)
        print(playing)
        y = 0
        guess = input("\nGuess a letter: ").lower()
        for x in range(lengthWord):
            letter = selectWord[x]
            if letter == guess:
                listWord[x] = letter
                y += 1
        if y == 0:
            lives -= 1
        print(stages[lives])

    if lives == 0:
        print(f"You lost.\nThe answer is {selectWord}")
    else:
        print(f"You win!\nThe answer is {selectWord}")

    choice = input("\nDo you want to play again? (y or n): ").lower()

print("Thank you and goodbye!")

