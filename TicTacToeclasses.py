import random
import time
import pprint

class Game(object):
    def __init__(self, piece):
        self.piece = piece
        self.board =  {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
        # self.board =  {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
        self.playerOne = "1"
        self.playerTwo = "2"
        
    def playerMove(self):
        if "-" not in self.board.values():
                user_input = input("The game is a tie! Would you like to play again?")
                user_input = user_input.lower()
                if user_input in("y", "yes"):
                    print("lets play again")
                    self.board =  {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
                    # self.playerMove()
                else:
                    print("Thanks for playing! Quitting the game.")
                    exit()
                
            
                # self.playerInput()
                            

        

    def playerInput(self):
        position = self.setPosition(self.playerOne) #this sets the position for player 1
        print("Position = " + str(position)) # This prints the position that player 1 chooses
        if self.board.get(position) == "-":
            self.board[position] = self.piece
            print(self.board)
            self.playerMove()
        else:
            print("That position already has a piece. Please choose another.")
            print(self.board)
            # self.playerMove()
            self.playerInput()
        self.playerMove()
        self.playerTwoTurn()


    def playerTwoTurn(self):
        position = self.setPosition(self.playerTwo) #this sets the position for player 2
        if self.piece == "X":
            playerTwoPiece = "O"
        else:
            playerTwoPiece = "X"
        
        if self.board.get(position) == "-":
            self.board[position] = playerTwoPiece
            print(self.board)
            self.playerMove()

        # if self.board[position] == "-":
        #     self.board[position] = playerTwoPiece
        #     print(self.board)
        #     self.playerMove()
        else:
            print("That position already has a piece. Please choose another.")
            print(self.board)
            self.playerTwoTurn()
        self.playerMove()
        self.playerInput()

    def setPosition(self, player):
        positionInput = input("Player " + str(player) + " please choose a spot: ")
        while True:
            if positionInput in self.board.keys():
                print("This input is a position on the board")
                return positionInput
            if positionInput not in self.board.keys():
                print("This is an incorrect input. Please input a number 0-9.")
                self.setPosition
            return positionInput
        # return positionInput
        # print(type(positionInput))
        # if positionInput != int:
        #     print("This isnt an integer")
        # else:
        #     return positionInput
        # while positionInput != int:
        #     print("This is not a number")
        
        


#if the input is a number, check the dictionary key and assign the players piece to that vaue
#if the input is a number isnt a key in teh dictionary, tell the user that number is not a position on the board
#if the user inputs a character that isnt a number, tell them to enter a number between 0-9. 

        # self.board.keys()
        # while True:
        #     positionInput = input("Player " + str(player) + " please choose a spot: ")
        #     if positionInput.isdigit():
        #     positionInput = int(positionInput)
        #     break
        #     if positionInput != self.board.keys():
        #         print("This isnt one of the positions please try again")
        #         break
        #     return positionInput
        # else:
        #     print("This isnt a number")
        # return self.setPosition


    

game1 = Game("O")
game1.playerInput()

 # playerChoice = input("Starting the first round. Who will be Player 1? ")
        # if self.player == 1:
        #     self.playerTwo = 2
        # else:
        #     self.playerTwo = 1
        # print(self.playerTwo)


#add functionality to have the user reinput a command if the input is not X or O, also y or yes
#add functionlity that allows the players to switch sides
#add pattern functionality to determine winner
#add functionality to print how many times each player won during this set of games before the game is quit


# def setPosition(self, player):
#         positionInput = input("Player " + str(player) + " please choose a spot: ")
#         if positionInput.isdigit():
#             positionInput = int(positionInput)
#             if positionInput != self.board.keys():
#                 print("This isnt one of the positions please try again")
#             return positionInput
#         else:
#             print("This isnt a number")
#         return self.setPosition


#if the input is a number but is not one of the keys, print somethign, and then check again