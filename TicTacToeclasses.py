#current problems
#The game is not taking the correct turns switching sides after the game is over
#need to figure out how to check if its 3 Xs or 3 Os, the player currently assigned to X or O wins that round
#add functionality to print how many times each player won during this set of games before the game is quit
#combine piece information into a method
import random
import time
import pprint

class Game(object):
    def __init__(self, piece):
        self.piece = piece
        self.board =  {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
        self.playerOne = "1"
        self.playerTwo = "2"
        self.p1Counter = 0
        self.p2Counter = 0
        
    def playerMove(self):
        print(self.piece)
        #if the value of key 1 2 and 3 is equal to X or O then print("something")
        #if key (1, 2, 3) in self.board == "X" or "O" then print()
        
        if self.board["1"] == "X" and self.board["2"] == "X" and self.board["3"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["1"] == "O" and self.board["2"] == "O" and self.board["3"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["1"] == "X" and self.board["4"] == "X" and self.board["7"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["1"] == "O" and self.board["4"] == "O" and self.board["7"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["1"] == "X" and self.board["5"] == "X" and self.board["9"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["1"] == "O" and self.board["5"] == "O" and self.board["9"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["2"] == "X" and self.board["5"] == "X" and self.board["8"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["2"] == "O" and self.board["5"] == "O" and self.board["8"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["3"] == "X" and self.board["5"] == "X" and self.board["7"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["3"] == "O" and self.board["5"] == "O" and self.board["7"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["3"] == "X" and self.board["6"] == "X" and self.board["9"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["3"] == "O" and self.board["6"] == "O" and self.board["9"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["4"] == "X" and self.board["5"] == "X" and self.board["6"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["4"] == "O" and self.board["5"] == "O" and self.board["6"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        if self.board["7"] == "X" and self.board["8"] == "X" and self.board["9"] == "X":
            print("Player 1 wins!")
            self.p1Counter = self.p1Counter + 1
            print(self.p1Counter)
            self.gameOver()
        if self.board["7"] == "O" and self.board["8"] == "O" and self.board["9"] == "O":
            print("player 2 wins!")
            self.p2Counter = self.p2Counter + 1
            print(self.p2Counter)
            self.gameOver()
        
        self.tieGame()
                                          
    def gameOver(self):
        print("This is a counter for Player 1 wins: " + str(self.p1Counter))
        print("This is a counter for Player 2 wins: " + str(self.p2Counter))
        user_input = input("The game is over! Player X wins! Would you like to play again or quit?")  
        user_input = user_input.lower()
        if user_input in ("y", "yes"):
            print("Lets play again. Players switching sides.")
            print(self.piece)
            self.board =  {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
            if self.piece == "X":
                self.piece = "O"
            if self.piece == "O":
                self.piece = "X"
            # self.playerMove()
        else:
            print("Thanks for playing! Quitting the game. The final score was Player 1: " + str(self.p1Counter) + "Player 2: " + str(self.p2Counter))
            exit()
        
    def tieGame(self):
        if "-" not in self.board.values():
            user_input = input("The game is a tie! Would you like to play again?")  
            user_input = user_input.lower()
            if user_input in ("y", "yes"):
                print("Lets play again. Players switching sides.")
                print(self.piece)
                self.board =  {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
                if self.piece == "X":
                    self.piece = "O"
                if self.piece == "O":
                    self.piece = "X"
                # self.playerMove()
            else:
                print("Thanks for playing! Quitting the game.")
                exit()

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
        if self.piece == "O":
            playerTwoPiece = "X"
        # else:
        #     playerTwoPiece = "X"
        
        if self.board.get(position) == "-":
            self.board[position] = playerTwoPiece
            print(self.board)
            self.playerMove()

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

