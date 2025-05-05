import random
from guessthenumberart import logo

print(logo)

def compare(user_input):
    if user_input==COMPUTER_NUMBER:
        print(f"You got it!. The answer is {user_input}")
        return True
    elif user_input> COMPUTER_NUMBER:
        print("Too High")
        return False
    elif user_input< COMPUTER_NUMBER:
        print("Too Low")
        return False

def get_input(count):
    continue_game=False
    while not continue_game:
        for i in range(count):
            # print(i)
            print(f"You have {count} attempts remaining to guess the number:")
            count -= 1
            my_guess = int(input("Make a guess: "))
            continue_game=compare(my_guess)
            if continue_game == True:
                return
        print("You ran out of attempts, you lose!")
        return


print("Welcome to the Number Guessing Game!\n")
print("I am thinking of a number between 1 to 100.")
COMPUTER_NUMBER = random.randint(1,100)
# print(f"Computer Picked Number is: {COMPUTER_NUMBER}")
difficulty_level=input("Choose the difficulty. Type 'easy' or 'Hard': ").lower()

if difficulty_level == 'easy':
    attempts=10
else:
    attempts=5

get_input(attempts)


