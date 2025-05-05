from blackjacklogo import logo
import random

def deal_card():
    '''This will return a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent has balckjack"
    elif u_score == 0:
        return "Win with balckjack"
    elif u_score>21:
        return "You went over, you loose"
    elif c_score>21:
        return "Opponent went over, you win"
    elif u_score>c_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score=-1
    computer_score=-1 #we are using these 2 lines to avoid the warning in line no 46 while computer_score!=0 and computer_score<17:
    # because computer_score was defined the while loop while not is_game_over, just in case if skip this while loop, the value for
    # computer_score and user_score will be undefined.
    # if we try to pass the value as 0, then it will be blackjack
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"\tYour cards {user_cards}: , current score is {user_score} ")
        print(f"\tComputer's first card : {computer_cards[0]}")

        if user_score ==0 or computer_score ==0 or user_score>21:
            is_game_over=True
        else:
            continue_game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            if continue_game =="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand {user_cards}: , final score is {user_score} ")
    print(f"Computer's final hand : {computer_cards}, final score is {computer_score} ")
    print(compare(user_score,computer_score))

while input("Want to play the balckjack game, Type 'y' or 'n' :") == 'y':
    print("\n"*20)
    play_game()
# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.



# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

