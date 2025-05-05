from higher_or_lower_art import logo, vs
from higher_lower_data import data
import random

# a = random.choice(data)
# b = random.choice(data)
# # the below code will make sure that both a and b won't have the same data
# while a['name'] == b['name']:
#     b = random.choice(data)



def randomvalues(a,b):
    if a =='':
        a = random.choice(data)
        b = random.choice(data)

    # the below code will make sure that both a and b won't have the same data
    while a['name'] == b['name']:
        b = random.choice(data)
    return a, b



def compare(x, y):
    if x['follower_count'] > y['follower_count']:
        a=x
        b = random.choice(data)
        a,b =randomvalues(a,b)
        return 'a',a,b
    elif x['follower_count'] < y['follower_count']:
        a=y
        b=random.choice(data)
        a, b = randomvalues(a, b)
        return 'b',a,b



def game():
    score = 0
    a = ''
    b = ''
    continuegame=True
    a,b=randomvalues(a,b)
    while continuegame:
        print(logo)
        print(f"a and b values A: {a} and B: {b}")
        print(f"Compare A: {a['name']},a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']},a {b['description']}, from {b['country']}")
        user_input=input("Who has more followers? Type 'A' or 'B': ").lower()
        result,a,b=compare(a, b)

        if result == user_input:
            score+=1
            print(f"You're right ! Current Score {score}")
        else:
            print(f"Sorry, that's wrong. Final Score {score}")
            continuegame= False



game()
