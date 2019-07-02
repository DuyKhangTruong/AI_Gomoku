class Board:
    def __init__(self): #15x15 board
        self.row = 15
        self.column = 15
        self.config = [[0*x for x in range(self.row)] for y in range(self.column)] #create a 15x15 board

    def DrawBoard(self):
        horizontal_sym = '-------------------------------'
        for i in range(self.column):
            horizontal_sym += '\n' + '|'
            for j in range(self.row):
                pos = self.config[i][j]
                if pos == 0:
                    pos = ' '
                horizontal_sym += str(pos) + '|'
            #horizontal_sym += '\n' +'-------------------------------'
        horizontal_sym += '\n-------------------------------'
        return horizontal_sym





