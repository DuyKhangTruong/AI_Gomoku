# author: Khang Nguyen&TheA
from policy import Policy
from board import Board
import math


class AI:
    def __init__(self, Computer):
        self.shape = Computer
        self.computer = Policy(self.shape)
        self.player = Policy("X")

    def Opponent(self):
        if self.shape == "X":
            return "O"
        return "X"

    # Check if there is any spaces left on board
    def moveLeft(self, board):
        for i in range(9):
            for j in range(9):
                if board.config[i][j] == 0:
                    return True

        return False

    # Check if the maxPlayer or minPlayer win or not
    def Evaluate(self, board, maxPlayer, x, y):
        if maxPlayer:
            if self.computer.checkWin(board, x, y):
                return 10
        else:
            if self.player.checkWin(board, x, y):
                return -10

        return 0

    #
    def MiniMax(self, board, depth, maxPlayer, alpha, beta, x, y, Score):
        score = self.Evaluate(board, not (maxPlayer), x, y)
        # print("board")
        # print(board.config)
        # print(depth)
        if depth == 4:
            return Score

        if score == 10:
            #print("The maxPlayer has won")
            #print(score - depth)
            return score - depth
        elif score == -10:
            #print("The minPlayer has won")
            # print(score)
            #print(score + depth)
            return score + depth

        if self.moveLeft(board) == False:
            #print("The board is full")
            return 0

        if maxPlayer:
            best = -10000000
            for i in range(9):
                for j in range(9):
                    if board.config[i][j] == 0:
                        board.config[i][j] = self.shape
                        score = self.MiniMax(
                            board, depth + 1, not (maxPlayer), alpha, beta, i, j, Score=score)
                        best = max(best, score)
                        alpha = max(alpha, best)
                        board.config[i][j] = 0
                        if beta <= alpha:
                            break
            return best

        else:
            best = 10000000
            for i in range(9):
                for j in range(9):
                    if board.config[i][j] == 0:
                        board.config[i][j] = "X"
                        score = self.MiniMax(
                            board, depth + 1, not (maxPlayer), alpha, beta, i, j, Score=score)
                        best = min(best, score)
                        beta = min(beta, best)
                        board.config[i][j] = 0
                        if beta <= alpha:
                            break
            return best

    def findBestMove(self, board):
        bestVal = -1000
        bestCol = -1
        bestRow = -1
        Score = int()
        # print("board")
        # print(board.config)
        # print(self.Opponent())
        for x in range(9):
            for y in range(9):
                if board.config[x][y] == 0:
                    board.config[x][y] = self.shape
                    # print("before")
                    # print(board.config)
                    # print(x)
                    # print(y)
                    currentVal = self.MiniMax(
                        board, 0, False, -math.inf, math.inf, x, y, Score)
                    board.config[x][y] = 0
                    # print("after")
                    # print(board.config)
                    # print(x)
                    # print(y)
                # print("Current Val")
                # print(currentVal)
                    print(currentVal)
                    if currentVal > bestVal:
                        bestVal = currentVal
                        bestRow = x
                        bestCol = y
                # print("Final")
                # print(board.config)
                # print(x)
                # print(y)
        print("the best value: " + str(bestVal))
        print("computer choose the row: " + str(bestRow))
        print("computer choose the column: " + str(bestCol))
        # print(board.config)

        return [bestRow, bestCol]

    def computerMove(self, board, x, y):
        # move = self.findBestMove(board)
        # x, y = move[0], move[1]
        # print("x,y")
        # print(x)
        # print(y)
        # print(board.config)
        self.computer.MakeMove(board, x, y)

    # Check if the computer win
    def isWin(self, board, x, y):
        return self.computer.checkWin(board, x, y)
