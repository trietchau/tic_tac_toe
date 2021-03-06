import random
import sys    
import time

def human():
    """
    Human play option, execute tic tac toe for 2 players
    function called after user type "human"
    """
    table = [    
        "-", "-", "-",     
        "-", "-", "-",    
        "-", "-", "-", 
        ]
    choices = choice()
    turn = [0,1,2,3,4,5,6,7,8]

    # while table still have available space, run until all boxes are filled
    while len(turn) != 0:
        
        # Player1's turn
        move_index, turn = table_check(table, turn)   # Check if the index is valid
        table[move_index] = choices[0]                # Fill X or O to the table base on the index chosen
        display_board(table)                          # Display to let them see for 2nd player's turn

        # The game cannot be won unless 5 moves has been played, so when turn has been reduced to 4 moves or less, check win
        # Check win before tie since last move might make it a win
        if len(turn) <= 4:
            win_condition, player = win_check(table)
            if win_condition == True:
                print(f"\nPlayer \"{player}\" won!!\nThanks for playing!")
                retry()

        # Player 1 will be the one who finish the game, so after filling every turn of player 1
        # we need to check if it's the last turn, if yes than break
        if len(turn) == 0:
            break
        
        # Player2's turn
        move_index, turn = table_check(table, turn)   # Check if the index is valid
        table[move_index] = choices[1]                # Fill X or O to the table base on the index chosen
        display_board(table)                          # Display to let them see for 2nd player's turn

        # The game cannot be won unless 5 moves has been played, so when turn has been reduced to 4 moves or less, check win
        if len(turn) <= 4:
            win_condition, player = win_check(table)
            if win_condition == True:
                print(f"\nPlayer \"{player}\" won!!\nThanks for playing!")
                retry()
    
    print("\nDRAW!")
    retry()


def bot():
    """
    Bot play option, execute tic tac toe for 1 player
    function called after user type "bot"
    """
    table = [    
        "-", "-", "-",     
        "-", "-", "-",    
        "-", "-", "-", 
        ]
    choices = choice()
    turn = [0,1,2,3,4,5,6,7,8]
    
    while len(turn) != 0:
        
        # Player1 turn
        move_index, turn = table_check(table, turn)   # Check if the index is valid
        table[move_index] = choices[0]                # Fill X or O to the table base on the index chosen
        display_board(table)                          # Display to let them see for 2nd player's turn

        # The game cannot be won unless 5 moves has been played, so when turn has been reduced to 4 moves or less, check win
        # Check win before tie since last move might make it a win
        if len(turn) <= 4:
            win_condition, win = win_check(table)
            if win_condition == True:
                print(f"\nYou won!!!\nThanks for playing!")
                retry()

        # "X" will be the one who finish the game, so after filling the X into the table
        # We need to check if it's the last turn, if yes than break
        if len(turn) == 0:
            break
        
        # Bot's turn
        move_index = random.choice(turn)  # Bot moves can just be chosen randomly from the
        turn.remove(move_index)           # available moves from turn, so doesnt need to table_check()
        table[move_index] = choices[1]    # Fill X or O to the table base on the index chosen
        print("Bot is thinking....")
        time.sleep(random.randint(1,2))   # Make it realistic

        # The game cannot be won unless 5 moves has been played, so when turn has been reduced to 4 moves or less, check win
        if len(turn) <= 4:
            win_condition, win = win_check(table)
            if win_condition == True:
                display_board(table)
                print(f"The bot won!!!\nThanks for playing!")
                retry()


    print("\nDRAW!")
    retry()


def table_check(table: list, turn: list) -> (int, list):
    """
    Check tic tac toe turn, make sure no duplicate or out of range input
    take in table to display_board() and turn to check it against the player's move to see if it's unavailable
    return index of the player's move and the list of the remaining spot yet to be chosen
    """

    display_board(table)
    # - 1 to fit it to the real index of 0-8
    index = int(input("\nPlease enter a number from 1-9 to fill the table: ")) - 1
    
    # If user enter invalid number or numbers that are already filled:
    while index not in turn:

        if index > 8 or index < 0:
            display_board(table)
            print("Not a valid number, please try again: ")
            index = int(input("Enter a number from 1-9: ")) - 1
        else:
            display_board(table)
            print("Square already filled, please pick a different number: ")
            index = int(input("Enter a number from 1-9: ")) - 1          

    turn.remove(index)
    return index, turn

        
def win_check(table: list) -> (bool, str):
    """
    Check after every turn if a player has won
    """
    # Combinations that would lead to a win
    win_list = [
        [0,1,2], [3,4,5],
        [6,7,8], [0,3,6],
        [1,4,7], [2,5,8],
        [0,4,8], [6,4,2],
    ]
    for line in win_list:
        # Check rows, columns, and diagonals
        combination = set([table[line[0]], table[line[1]], table[line[2]]])

        if len(combination) == 1 and combination != {"-"}: # Which mean we have a straight line of either X or O
            #unpack comb (which is 1 item), which is either "X" or "O" to know who won
            return True, *combination
    else:
        return False, None


def retry():
    for attempt in range(3):
        answer = input("Do you want to play again? y/n: ")

        if answer.lower() == "y" or answer.lower() == "yes":
            game()

        elif answer.lower() == "n" or answer.lower() == "no":
            print("\nThanks for playing!!!\n")
            # If the user choose to play again, the for loop will stay and stack over each other, so after a no answer, sys.exit()
            sys.exit()

        elif attempt < 2:
            print(f"\nYou didn't enter the correct choices, please try again, you have {2-attempt} attempt(s) left.")

    print("\nYou didnt enter 'y' or 'n', so the game will end. Thanks for playing!\n")
    # sys.exit() to prevent stacking from for loop because the user might play multiple time and the remaining loop(s) will stay
    sys.exit()


def choice() -> list:
    """
    Let player choose if they want "X" or "O"
    """
    p1 = input("Choose X or O for player1: ")

    while p1 != "X" and p1 != "O":
        p1 = input("Invalid, choose either \"X\" or \"O\": ")

    if p1 == "X":
        # ["X", "O"]
        return [p1,"O"]
    else:
        # ["O", "X"]
        return [p1, "X"]


def display_board(table: list):
    print("\n")
    print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
    print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
    print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
    print("\n")


def game():
    play_option = ""
    while play_option.lower() != "human" and play_option.lower() != "bot":     
        play_option = input("Please type 'human' or 'bot': ") 
    
    if play_option == "human":     
        human()
    else:
        bot()


if __name__ == "__main__":
    game()