import random 
import sys

print('Welcome To Snake Ladder Game'.center(50,"*"))

def dice():
    return random.randint(1,6)

def first_player_turn():
    global player1_score
    player1_status = input(f"{player1}: want to[C]ontinue or [S]top:").upper()
    if player1_status=='C':
        player1_turn = dice()
        player1_score+=player1_turn
        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f"\n{player1}'s turn: \n Dice: {player1_turn} \n----Snake Bite----\nBoard position:{player1_score}")
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f"\n{player1}'s turn:\nDice:{player1_turn}\n****Ladder****\nBoard position:{player1_score}")
        else:
            print(f"\n{player1}'s turn:\nDice:{player1_turn}\nBoard position: {player1_score}")
    elif player1_status=='S':
        print(f'\n{player1} quit the game.\n{player2} won the game!!!')
        sys.exit()


def second_player_turn():
    global player2_score
    player2_status = input(f"{player2}: want to [C]ontinue or [S]top: ").upper()
    if player2_status=='C':
        player2_turn = dice()
        player2_score+=player2_turn
        print(f"{player2}'s turn: \nDice:{player2_turn} ")
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f"\n{player2}'s turn: \n Dice: {player2_turn} \n----Snake Bite----\nBoard position:{player2_score}")
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f"\n{player2}'s turn:\nDice:{player2_turn}\n****Ladder****\nBoard position:{player2_score}")
        else:
            print(f"\n{player2}'s turn:\nDice:{player2_turn}\nBoard position: {player2_score}")
    elif player2_status=='S':
        print(f'\n{player2} quit the game. \n{player1} won the game!!!')
        sys.exit()
        






player1 = input("enter the player-1:")
player2 = input("enter the player-2:")

player1_score=0
player2_score=0

winning_point=100


snakes= {99:23,34:56,67:32,89:9}
ladders={7:19,12:56,34:78,54:98}

while player1_score<winning_point and player2_score<winning_point:
    first_player_turn()
    second_player_turn()
else:
    if player1_score>player2_score:
        print(f"\n\n{player1} Win the game!!!!!!")
    elif player1_score==player2_score:
        print(f"\n\nTie!!!!!!")
    else:
        print(f"\n\n{player2} Win the game!!!!!!")
