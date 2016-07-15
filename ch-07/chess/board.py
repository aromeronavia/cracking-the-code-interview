from pawn import Pawn
from empty_coord import EmptyCoord
from board_printer import printBoard

class Board:
    def __init__(self):
        self._initializeBoard()

    def _initializeBoard(self):
        self.board = [[EmptyCoord(i, j) for i in range(8)] for j in range(8)]
        self.initializeWhitePieces()
        self.initializeBlackPieces()

    def initializeWhitePieces(self):
        self.board[0][0] = Pawn(0, 0, 'white')
        self.board[0][1] = Pawn(0, 1, 'white')
        self.board[0][2] = Pawn(0, 2, 'white')
        self.board[0][3] = Pawn(0, 3, 'white')
        self.board[0][4] = Pawn(0, 4, 'white')
        self.board[0][5] = Pawn(0, 5, 'white')
        self.board[0][6] = Pawn(0, 6, 'white')
        self.board[0][7] = Pawn(0, 7, 'white')
        self.initializeWhitePawns()

    def initializeBlackPieces(self):
        self.board[7][0] = Pawn(7, 0, 'black')
        self.board[7][1] = Pawn(7, 1, 'black')
        self.board[7][2] = Pawn(7, 2, 'black')
        self.board[7][3] = Pawn(7, 3, 'black')
        self.board[7][4] = Pawn(7, 4, 'black')
        self.board[7][5] = Pawn(7, 5, 'black')
        self.board[7][6] = Pawn(7, 6, 'black')
        self.board[7][7] = Pawn(7, 7, 'black')
        self.initializeBlackPawns()

    def initializeWhitePawns(self):
        for i in range(8):
            self.board[1][i] = Pawn(1, i, 'white')

    def initializeBlackPawns(self):
        for i in range(8):
            self.board[6][i] = Pawn(6, i, 'black')

    def printBoard(self):
        printBoard(self.board)

if __name__ == '__main__':
    board = Board()
    board.printBoard()
