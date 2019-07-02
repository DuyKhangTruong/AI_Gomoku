#author: Khang Nguyen&TheA
from policy import Policy
from board import Board


class AI:
    def __init__(self, Computer):
        self.shape = Computer
        self.computer = Policy(self.shape)

    def Opponent(self):
        if self.shape == "X":
            return "O"
        return "X"

    # Check if there is any spaces left on board
    def moveLeft(self, board):
        for i in range(15):
            for j in range(15):
                if board.config[i][j] == ' ':
                    return True

        return False

    # Check if the maxPlayer or minPlayer win or not
    def Evaluate(self, board, maxPlayer, x, y):
        if maxPlayer:
            if self.computer.checkWin(board, x, y):
                return 10
        else:
            if self.computer.checkWin(board, x, y):
                return -10

        return 0

    #
    def MiniMax(self, board, depth, maxPlayer, x, y):
        score = self.Evaluate(board, maxPlayer, x, y)

        if score == 10:
            print("The maxPlayer has won")
            return score - depth
        elif score == -10:
            print("The minPlayer has won")
            return score + depth
        else:
            print("Nobody has won yet")
            return score

        if self.moveLeft(board):
            print("The board is full")
            return 0

        if maxPlayer:
            best = -1000000
            for x in range(15):
                for y in range(15):
                    if board.config[x][y] == ' ':
                        board.config[x][y] = self.shape
                        best = self.MiniMax(
                            board, depth + 1, not (maxPlayer), x, y)

                    board.config[x][y] = ' '
            return best

        else:
            best = 10000000
            for i in range(15):
                for j in range(15):
                    if board.confsig[i][j] == ' ':
                        board.config[i][j] = self.Opponent()
                        best = self.MiniMax(
                            board, depth + 1, not (maxPlayer), i, j)
                    board.config[i][j] = " "
            return best

    def findBestMove(self, board):
        bestVal = -100
        bestCol = -1
        bestRow = -1

        for x in range(15):
            for y in range(15):
                currentVal = self.MiniMax(board, 0, True, x, y)
                if currentVal > bestVal:
                    bestVal = currentVal
                    bestRow = x
                    bestCol = y
        print("the best value: " + str(bestVal))
        print("computer choose the row: " + str(bestRow))
        print("computer choose the column: " + str(bestCol))

        return [bestRow, bestCol]

    def computerMove(self, board):
        move = self.findBestMove(board)
        x, y = move[0], move[1]
        self.computer.MakeMove(board, x, y)

    # Check if the computer win
    def isWin(self, board, x, y):
        return self.computer.checkWin(board, x, y)
