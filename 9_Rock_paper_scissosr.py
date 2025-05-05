import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

customer_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper 0r 2 for Scissors.\n"))
system_input=random.randint(0,2)
# if customer_input==0:
#     print(rock)
# elif customer_input==1:
#     print(paper)
# else:
#     print(scissors)

game_images = [rock, paper, scissors]
print(game_images[customer_input])

print("Computer chose:")
# if system_input==0:
#     print("It's Rock")
#     print(rock)
# elif system_input==1:
#     print("It's paper")
#     print(paper)
# else:
#     print(system_input)
#     print("It's scissors")
#     print(scissors)

print(game_images[system_input])
#
# if (customer_input == 0) and (system_input == 2):
#     print("You win")
# elif (customer_input == 2) and (system_input == 1):
#     print("you win")
# elif (customer_input == 1) and (system_input == 0):
#     print("You win")
# elif (customer_input == 2) and (system_input == 0):
#     print("Computer win")
# elif (customer_input == 1) and (system_input == 2):
#     print("Computer win")
# elif (customer_input == 0) and (system_input == 1):
#     print("Computer win")
# elif customer_input == system_input:
#     print("It's tie")

print('----------------------------')

# customer=0
# system=0
# if customer_input>system_input:
#     if (system_input == 0) and (customer_input == 2):
#         system=1
#     else:
#         customer = 1
# elif system_input>customer_input:
#     if (system_input == 2) and (customer_input == 0):
#         customer = 1
#     else:
#         system=1
# elif customer_input==system_input:
#     system=1
#     customer=1
#
# if customer == system:
#     print("It's a Tie")
# elif customer>system:
#     print("You win")
# else:
#     print("Computer Win")



if customer_input >= 3 or customer_input < 0:
  print("You typed an invalid number, you lose!")
elif customer_input == 0 and system_input == 2:
  print("You win!")
elif system_input == 0 and customer_input == 2:
  print("You lose")
elif system_input > customer_input:
  print("You lose")
elif customer_input > system_input:
  print("You win!")
elif system_input == customer_input:
  print("It's a draw")