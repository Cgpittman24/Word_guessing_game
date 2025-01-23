#define title of game
title = "Word Guessing Game"
#open the file containing the list of words
with open("words.txt", 'r') as word_game:
    line = word_game.readlines()

#generating a random word from the list of words
from random import randint
word = line[randint(0, len(line) - 1)] 

#defining tracking variables for the program 
guesses_not_in_word = []
max_turns = 15
turns_taken = 0
correct_guesses = []

#welcome the player to the game using title and inform them of the rules
print(f"Welcome to the {title}!")
print("There are 5 letters in the word.")
print(f"You have {max_turns} turns to guess the word.")
print("Good luck!")

while turns_taken < max_turns:
    #ask the player to guess a letter
    guess = input("Guess a letter: ")
    #check if the letter is in the word
    if guess in word:
        print("Correct!")
        correct_guesses.append(guess)

    #if the letter is not in the word, inform the player and add the letter to the tracking list
    else:
        print("INCORRECT!")
        guesses_not_in_word.append(guess)
        turns_taken += 1
    #if the player has guessed all the letters in the word, inform them and end the game
    if set(word) == set(guess):
        print(f"Congratulations! You have guessed the word: {word}")
        break
    #if the player has used all their turns, inform them and end the game
    if turns_taken == max_turns:
        print(f"Sorry, you have run out of turns. The word was: {word}")
        break
    #inform the player of the letters they have guessed and the number of turns they have left
    left = 5 - len(correct_guesses)
    print(f"Letters guessed: {guesses_not_in_word}")
    print(f"Turns left: {max_turns - turns_taken}")
    #imform the player of what that have already guessed correctly and how many letters are left
    print(f"Correct guesses: {correct_guesses}")
    print(f"Letters left: {left}")