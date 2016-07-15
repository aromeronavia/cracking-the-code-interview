columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']

class Board:
    def __init__(self):
        self._initializeBoard()

    def _initializeBoard(self):
        self.board = {}
        for i in rows:
            for j in columns:
                self.board[j + i] = ''

    def printBoard(self):
        for (key, value) in self.board:
            print key, value

board = Board()
board.printBoard()
