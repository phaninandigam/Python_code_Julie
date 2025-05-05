#Step 1
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)

print(f"Your choosen word is {chosen_word}")
display=[]
for word in chosen_word:
    display+="_"

print(display)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# print(guess)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# x=0
# for letter in chosen_word:
#     if letter == guess:
#         display.insert(x,guess)
#         display.pop(x+1)
#     x+=1
# print(display)
# print("----------------------------")
lives=6
hang=True
end_of_game=False
while not end_of_game:
    hang = True
    guess = input("Please guess a letter: ").lower()
    print("-------------------")
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
            hang=False
    print(display)

    if "_" not in display:
        print("You win")
        end_of_game=True
    elif lives>0 and hang == True:
        print(stages[lives-1])
        lives -= 1
        if lives==0:
            print("You lost")
            end_of_game=True
    # elif lives>0 and hang == False:

