from board import Board


class Policy:
    def __init__(self, shape):
        self.shape = shape

    def MakeMove(self, board, x, y):  # mMake a move on board
        board.config[x][y] = self.shape
        # print(board.DrawBoard())

    def CheckLegal(self, board, x, y):  # Check if that move is valid
        if x > 14 or x < 0:
            return False
        if y > 14 or y < 0:
            return False

        if (board.config[x][y] != 0):
            return False

        return True

    def checkWin(self, board, x, y):
        return self.CheckVe(board, x, y) or self.CheckHoz(board, x, y) or self.CheckDiag1(board, x, y) or self.CheckDiag2(board, x, y)

    def CheckHoz(self, board, x, y):  # Check if the player has 5 in the row
        Number_of_shape = 1
        z = y + 1
        y -= 1

        # Check forward starting from the coordinate of the latest move
        while z <= 14 and board.config[x][z] == self.shape:
            Number_of_shape += 1
            z += 1
            if Number_of_shape == 5:
                return True
        # Check backward starting from the coordinate of the latest move
        while y >= 0 and board.config[x][y] == self.shape:
            Number_of_shape += 1
            y -= 1
            if Number_of_shape == 5:
                return True

        return False

    def CheckVe(self, board, x, y):  # Check if the player has 5 in column
        Number_of_Shape = 1
        z = x + 1
        x -= 1
        # Check downward starting from the coordinate of the latest move
        while z <= 14 and board.config[z][y] == self.shape:
            Number_of_Shape += 1
            z += 1
            if Number_of_Shape == 5:
                return True

        # Check upward starting from the coordinate of the latest move
        while x >= 0 and board.config[x][y] == self.shape:
            Number_of_Shape += 1
            x -= 1
            if Number_of_Shape == 5:
                return True
        return False

    def CheckDiag1(self, board, x, y):
        Number_of_Shape = 1
        i, j = x, y
        i += 1
        j -= 1
        x -= 1
        y += 1

        while (i <= 14 and j >= 0) and board.config[i][j] == self.shape:
            Number_of_Shape += 1
            i += 1
            j -= 1
            if Number_of_Shape == 5:
                return True
        # print(Number_of_Shape)
        while (x >= 0 and y <= 14) and board.config[x][y] == self.shape:
            Number_of_Shape += 1
            x -= 1
            y += 1
            if Number_of_Shape == 5:
                return True
        return False

    def CheckDiag2(self, board, x, y):
        Number_of_Shape = 1
        i, j = x, y
        i -= 1
        j -= 1
        x += 1
        y += 1

        while (i >= 0 and j >= 0) and board.config[i][j] == self.shape:
            Number_of_Shape += 1
            i -= 1
            j -= 1
            if Number_of_Shape == 5:
                return True
        while (x <= 14 and y <= 14) and board.config[x][y] == self.shape:
            Number_of_Shape += 1
            x -= 1
            y += 1
            if Number_of_Shape == 5:
                return True
        return False
