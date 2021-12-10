"""Rock Scissors Paper Game
The simple rules of the game is :
Rock beats scissors
Scissors beat paper
Paper beats rock"""
import random

N_GAMES = 3


def main():
    print_welcome()
    human_score = 0
    ai_score = 0
    for i in range(N_GAMES):
        ai_move = get_ai_move()
        human_move = get_human_move()
        # write the logic to find out who won based on the inputs
        winner = get_winner(ai_move, human_move)
        if winner == 'computer':
            ai_score = calculate_score(winner, ai_score)
            print("The total computer score is", ai_score)
        elif winner == 'human':
            human_score = calculate_score(winner, human_score)
            print("The total human score is", human_score)
        print("Computer move was:", ai_move)
        print("The winner is", winner)
    if ai_score > human_score:
        print("The computer is the final winner !")
    elif ai_score < human_score:
        print("The human is the final winner !")
    else:
        print("Its a tie !")


def calculate_score(winner, total_score):
    if winner == 'computer':
        total_score = total_score + 1
        return total_score
    if winner == 'human':
        total_score = total_score + 1
        return total_score
    else:
        return 0


def print_welcome():
    print("Welcome to the game of Rock Scissors Paper")
    print("You have", N_GAMES, "games to play with computer")
    print("Rock beats scissors")
    print("Scissors beat paper")
    print("Paper beats rock")
    print("-----------------------------------------------------")
    print("")


def get_ai_move():
    value = random.randint(1,3)
    if value == 1:
        return 'rock'
    if value == 2:
        return 'paper'
    else:
        return 'scissors'

def get_human_move():
    human_move = input("Enter your move:")
    while True:
        if check_valid_move(human_move):
            return human_move
        else:
            print("A valid option should be rock or paper or scissors..")
            human_move = input("Please enter a valid move:")


def check_valid_move(human_move):
    if human_move == 'rock' or human_move == 'paper' or human_move == 'scissors':
        return True
    else:
        return False


def get_winner(ai_move, human_move):
    """Return either ai human or tie"""
    if ai_move == human_move:
        return 'tie'
    if ai_move == 'rock':
        if human_move == 'scissors':
            return 'computer'
        elif human_move == 'paper':
            return 'human'
    elif ai_move == 'scissors':
        if human_move == 'rock':
            return 'human'
        elif human_move == 'paper':
            return 'computer'
    elif ai_move == 'paper':
        if human_move == 'rock':
            return 'computer'
        elif human_move == 'scissors':
            return 'human'


if __name__ == '__main__':
    main()
