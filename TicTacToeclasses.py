import random
import time
import pprint

class Game(object):
    def __init__(self, piece):
        self.piece = piece
        self.board =  {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
        self.playerOne = 1
        self.playerTwo = 2
        
    def playerMove(self):
        if "-" not in self.board.values():
                user_input = input("The game is a tie! Would you like to play again?")
                if user_input == "Y" or user_input == "Yes":
                    print("lets play again")
                    self.board =  {0: "-", 1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
                    # self.playerMove()
                else:
                    print("Thanks for playing! Quitting the game.")
                    return
                return
            
                # self.playerInput()
                            

        

    def playerInput(self):
        position = self.setPosition(self.playerOne)
        print("Position = " + str(position))
        if self.board[position] == "-":
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
        position = self.setPosition(self.playerTwo)
        if self.piece == "X":
            playerTwoPiece = "O"
        else:
            playerTwoPiece = "X"
        if self.board[position] == "-":
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
        positionInput = int(input("Player " + str(player) + " please choose a spot: "))
        return positionInput
        

    

game1 = Game("O")
game1.playerInput()

 # playerChoice = input("Starting the first round. Who will be Player 1? ")
        # if self.player == 1:
        #     self.playerTwo = 2
        # else:
        #     self.playerTwo = 1
        # print(self.playerTwo)