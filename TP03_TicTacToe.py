import os # import to use clear screen function
import sys
from termcolor import colored, cprint # import for color schemes
from colorama import Fore, Back, Style 

def game_title():
    # Change the text color and display the title of the game
    title = colored("\t\t\t\t------Tic-Tac-Toe------   ", "yellow", attrs=['bold'])
    print(title)
    # create a variable that displays the board using the doc string method for the use of multiple lines
    board = colored("""      
                                       |     |    
                                       |     |    
                                  _____|_____|_____
                                       |     |      
                                       |     |   
                                  _____|_____|_____
                                       |     |    
                                       |     |
                                       |     |      """, "yellow")
                                        
    print(board) # display the tic tac toe board 
    print()
    input("Press Enter to continue...") # Pause the the code until user presses Enter. 
game_title() # call the function

os.system("cls") # Clear the screen so it looks clean

def rules(): # Create a function that will display the rules of the game
    board_rules = colored("""      
                                       |     |    
                                    1  |  2  |  3  
                                  _____|_____|_____
                                       |     |      
                                    4  |  5  |  6
                                  _____|_____|_____
                                       |     |    
                                    7  |  8  |  9
                                       |     |      """, "yellow")
    rules_title = colored("----------------------------------RULES----------------------------------\n", "red", attrs=['bold'])
    game_rules = colored("\n1) This game is played on a 3 X 3 square baord."
    "\n2) First player picks their character to be either 'X' or 'O'."
    "\n3) The Player that picks 'X' will go first."
    "\n4) Select the corresponding number for your position as shown below."
    "\n5) The first player to get 3 in a row by vertical, horizontal or by diagonal will be the winner.\n"
    f"\n{board_rules}\n", "blue")
    rules_border = colored("-------------------------------------------------------------------------","red", attrs=['bold'])
    print(rules_title)
    print(game_rules)
    print(rules_border)
    print()
    input("Press Enter to continue...")
rules() # call the function

os.system("cls")

def start_message(): # Create a Game message to add some fun.
    lets_play = colored(
        """         \t\t   ====================================
           \t\t   |                                  |
           \t\t   ==========!!!LET'S PLAY!!!==========
           \t\t   |                                  |
           \t\t   ====================================\n""", "yellow" )
    print(lets_play)
    print()
    input("Press Enter to continue...")
start_message()

os.system("cls")

f = open("tictacttoe.txt", "a") # Open the txt doc for it to be appended

player1 = input("1st contender, enter your name: ") # Prompt users for their names
player2 = input("2nd contender, enter your name: ")

board = [" "] *10 # variable for the boards empty positions 

def user_input(): # create a function that askes the user to be "X" or "O"
    global player1 # use global variable to make changes to a variable in local context
    global player2
    p1 = input("Choose your character 'X' or 'O'. \n")

    while True: # Use a while loop Bool value to prevent the user from typing something other than "x" or "o"
        if p1.upper() == 'X': # Condition statement to determine the other players character.
            p1 = "X" 
            p2 = "O"
            print(f"You chose {p1.upper()}\n\n{player1} is {p1.upper()}\nand {player2} is {p2}.\n")
            print(f"{player1} goes first.\n")
            return p1, p2
            
        elif p1.upper() == 'O':
            p1 ="O"
            p2 = 'X'
            print(f"You chose {p1.upper()}. \n\n{player1} is {p1.upper()} \nand {player2} is {p2}.\n")
            print(f"{player2} goes first.\n")
            player1, player2 = player2, player1 # swap the players so that player1 is player2
            return p1, p2

        else: # This will equal false and loop the message back using the new statement
            p1 = input("Sorry, you must choose either 'X' or 'O': \n")
user_input()

def display_board(board): # This is the boards function and the corresponding numbers for the positions
    print("    |     |    ")
    print(" " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("____|_____|____")
    print("    |     |    ")
    print(" " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("____|_____|____")
    print("    |     |    ")
    print(" " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("    |     |    ")

def play_game(): # function to start the game and play
    global player1
    global player2
    players_move = "X" # The first move starts with "X" using the variable that can be changed to "O"
    count = 0 # count starts at 0
    current_player = player1.title() # create variable for current player and player 1 starts.
    player_position = {"X":[], "O":[]} # Creat a dictionary to record the positions entered

    for i in range(10): # loop throught the positions
        display_board(board) # display the board
        player_turn_message = colored(f"\n{current_player}, PICK A SPOT!", "green") # promt user their turn 
        print(player_turn_message)

        while True: # handling errors for fat fingered users
            try:
                player_pick = eval(input()) # use the eval function to evaluate the compiled input expression
                if board[player_pick] == " ": # condition statement to evaluate if the players pick is empty on the board
                    board[player_pick] = players_move # change the variable
                    player_position[players_move].append(player_pick) # add the players position to be recorded
                    count += 1 # increment by 1
                else: # make an else statement if the position is claimed already
                    occupied = colored(f"That place is already filled {current_player}.\n\t\tTry Again!", "red")
                    print(occupied)
                    continue
            except:
                error_msg = colored("Please input a number between 1 - 9.\n\t\tTry Again!", "red")                
                print(error_msg) 
                continue
            else:
                break
        
        if count >= 5: # condition statement for all possible wins
            if board[1] == board[2] == board[3] != " ": # if the board has positions 1, 2, 3  are not empty 
                winner(players_move) # with the same user character
                break 
            if board[4] == board[5] == board[6] != " ": # this is the same as previous lines
                winner(players_move)
                break
            if board[7] == board[8] == board[9] != " ":
                winner(players_move)
                break
            if board[1] == board[4] == board[7] != " ":
                winner(players_move)
                break
            if board[2] == board[5] == board[8] != " ":
                winner(players_move)
                break
            if board[3] == board[6] == board[9] != " ":
                winner(players_move)
                break
            if board[1] == board[5] == board[9] != " ":
                winner(players_move)
                break
            if board[3] == board[5] == board[7] != " ":
                winner(players_move)
                break

        if count == 9: # condition statement if the  game is a tie
            end_message = colored("\nGame Over\n\n\tTie!!\n\n", "red", attrs=['bold'])
            print(end_message)
            
        if players_move == "X": # alternate players
            players_move = "O"
            current_player = player2.title()
        else:
            players_move = "X"
            current_player = player1.title()
                   
    with open('tictacttoe.txt', 'a') as file: # open the TXT to be appended
        file.write("\n") # make a new line in the file so that it is not a long string
        file.write(str(player_position)) # add the recorded information in the txt file

        
    restart = input("\nDo want to play Again?(y/n): ") # prompt user if they would like to play again
    print()
    restart = restart.capitalize() # take the users input and make it capitalized
    if restart == "Y":
        for char in board: # loop throught the board to clear all the positions if they want to play again
            board[board.index(char)] = " "
        os.system("cls")
        print("\n\n")
        play_game()

def winner(players_move): # function for the winner of the game
    display_board(board)
    end_message = colored("\nGame Over.\n", "red", attrs=['bold'])
    print(end_message)
    if players_move == "X": # condition statement to determine who is the winner
        display_winner_boarder = colored("              =======================================", "yellow", attrs=['bold'])
        display_winner_sides = colored("              |                                     |", "yellow", attrs=['bold'])
        display_winner = colored(f"                         !!!{player1.title()} WON!!!             ", "yellow", attrs=['bold'])
        print(display_winner_boarder)
        print(display_winner_sides)
        print(display_winner)
        print(display_winner_sides)
        print(display_winner_boarder)        
    else:
        display_winner_boarder = colored("              =======================================", "yellow", attrs=['bold'])
        display_winner_sides = colored("              |                                     |", "yellow", attrs=['bold'])
        display_winner = colored(f"                         !!!{player2.title()} WON!!!           ", "yellow", attrs=['bold'])
        print(display_winner_boarder)
        print(display_winner_sides)
        print(display_winner)
        print(display_winner_sides)
        print(display_winner_boarder)

if __name__ == "__main__":
    play_game()

 

    

