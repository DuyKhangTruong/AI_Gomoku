from board import Board
from policy import Policy
from AI_Gomoku import AI


class Gomoku:
    def __init__(self):
        self.player1 = Policy("X")
        self.AI_Sec = AI("O")
        self.board = Board()
        self.computer = Policy(self.AI_Sec.shape)
# self is object itself (in this case gomoku)
# capitalize objects and classes

    def play(self):
        while True:
            turn_x = input("Player 1 turn x: ")
            turn_y = input("Player 1 turn y: ")

            while not (self.player1.CheckLegal(self.board, int(turn_x),         int(turn_y))):
                print("Please type again")
                turn_x = input("Player 1 turn x: ")
                turn_y = input("Player 1 turn y: ")
            self.player1.MakeMove(self.board, int(turn_x), int(turn_y))

            if self.player1.checkWin(self.board, int(turn_x), int(turn_y)):
                print("Player 1 wins")
                return

        #turn_x = input("Player 2 turn x: ")
        #turn_y = input("Player 2 turn y: ")

        # while not (self.player2.CheckLegal(self.board, int(turn_x), int(turn_y))):
            #turn_x = input("Player 2 turn x: ")
            #turn_y = input("Player 2 turn y: ")
            computerMove = self.AI_Sec.findBestMove(self.board)
            x, y = computerMove[0], computerMove[1]
            print(x)
            print(y)
            self.computer.MakeMove(self.board, x, y)
            if self.computer.checkWin(self.board, x, y):
                print("Computer wins")
                return


game = Gomoku()
game.play()
