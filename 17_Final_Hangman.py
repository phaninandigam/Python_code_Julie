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

chosen_word=random.choice(word_list)
print(f"The chosen word is : {chosen_word}")
display=[]
length_chosen_word=len(chosen_word)

for word in chosen_word:
    display+="_"
print(display)

end_of_game=False
lives=5

while not end_of_game:
    repeat_letter = 0
    guess=input("Enter the letter: ").lower()
    for position in range(length_chosen_word):
         if chosen_word[position]==guess:
             if "_" in display[position]:
                 display[position] = guess
             elif repeat_letter==0:
                 print(f"You've already entered the letter {guess}")
                 repeat_letter=1




    if "_" not in display:
        print("You won the game!")
        end_of_game=True

    if guess not in chosen_word:
        if lives>0:
            print(f"You chosse {guess}, it's not in the list")
            print("------------------")
            print(stages[lives])
            lives -= 1
        else:
            print(stages[lives])
            print("You lost game")
            end_of_game = True
    # print(display)
    print(f"{' '.join(display)}")
