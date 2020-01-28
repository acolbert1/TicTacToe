#when the code is executed have P1 and P2 take turns. P1 is always X P2 is always 0. 
#9 positions. so make a list or a variable or something for each position?
#When the user picks a space the CPU will pick a space and then the player can go.

#TODOLIST#
#1. have a checker to check if all the places are taken. if so that means the game was a tie.
#2. create patterns to check if someone won. example if X == 1 3 and 5 then they won.
#3. once the game ends restart and the other person goes first and they have the option to choose which piece they want?

import random
import time
import pprint
# print("- | - | -")
#         print("- | - | -")
#         print("- | - | -")

# class player:
#     def __init__(self, player):
#         self.player = player

#     def startgame(self):
#         PlayerOneCharacter = ""
#         PlayerOneCharacter =  input("Lets start a game of TicTacToe! Player one please choose a piece to play. Would you like to be X or O? ")
#         # PlayerOneCharacter = PlayerOneCharacter.lower()
#         while PlayerOneCharacter != "X" and PlayerOneCharacter != "O":
#             print("That character does not exist. Please choose an X or an O.")
#             PlayerOneCharacter = input("Please choose X or O: ")
#         if PlayerOneCharacter == "X":
#             print("Player One has chosen: " + PlayerOneCharacter + ". Player Two will be the O piece this game.")
#         else:
#             print("Player One has chosen: O. Player Two will be the X piece this game. Lets display the board.") #Create a if statement to display the other character based on what player 1 chooses.
#         time.sleep(2)
    
        


# class board:
#     def __init__(self):
#         # self.board = board
full_board = {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
def playerMoves():
    # full_board = {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
    playerOnePick = input("Player 1 please choose a spot: ")
    playerOnePick = int(playerOnePick)
   
    if full_board[playerOnePick] == "-":
        full_board[playerOnePick] = "X"
    else:
        print("That position already has a piece. Please choose another.")
        print(full_board) 
        return playerMoves()
    playerTwoMoves()
    
    # playerTwoPick = input("Player 2 please choose a spot: ")
    # playerTwoPick = int(playerTwoPick)
    # if full_board[playerTwoPick] == "-":
    #     full_board[playerTwoPick] = "O"
    #     print(full_board)
    # else:
    #     print("That position already has a piece. Please choose another.")
    #     print(full_board)   
    #     return playerTwoPick
    # return playerMoves()


def playerTwoMoves():
    playerTwoPick = input("Player 2 please choose a spot: ")
    playerTwoPick = int(playerTwoPick)
    if full_board[playerTwoPick] == "-":
        full_board[playerTwoPick] = "O"
        print(full_board)
    else:
        print("That position already has a piece. Please choose another.")
        print(full_board)   
        return playerTwoMoves()
    return playerMoves()


playerMoves()


#1. ask the user for input. the input is the position where they want to put there piece. i.e. if player inputs 5, they want to be in the middle of the grid.
#2. once the user puts in an input, check the dictionary to see if that key has a -. if it has a - that means that key is free to take a piece. 
#3. if that piece is not a -, then that space is not available to be played.


# p1 = player("Player 1")
# p2 = player("Player 2")
# p1.startgame()
