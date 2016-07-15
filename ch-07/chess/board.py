from pawn import WhitePawn, BlackPawn
from empty_coord import EmptyCoord
from board_printer import printBoard

class Board:
    def __init__(self):
        self._initializeBoard()

    def _initializeBoard(self):
        self.board = [[EmptyCoord(j, i) for i in range(8)] for j in range(8)]
        self.initializeWhitePieces()
        self.initializeBlackPieces()

    def initializeWhitePieces(self):
        self.board[0][0] = WhitePawn(0, 0)
        self.board[0][1] = WhitePawn(0, 1)
        self.board[0][2] = WhitePawn(0, 2)
        self.board[0][3] = WhitePawn(0, 3)
        self.board[0][4] = WhitePawn(0, 4)
        self.board[0][5] = WhitePawn(0, 5)
        self.board[0][6] = WhitePawn(0, 6)
        self.board[0][7] = WhitePawn(0, 7)
        self.initializeWhitePawns()

    def initializeBlackPieces(self):
        self.board[7][0] = BlackPawn(7, 0)
        self.board[7][1] = BlackPawn(7, 1)
        self.board[7][2] = BlackPawn(7, 2)
        self.board[7][3] = BlackPawn(7, 3)
        self.board[7][4] = BlackPawn(7, 4)
        self.board[7][5] = BlackPawn(7, 5)
        self.board[7][6] = BlackPawn(7, 6)
        self.board[7][7] = BlackPawn(7, 7)
        self.initializeBlackPawns()

    def initializeWhitePawns(self):
        for i in range(8):
            self.board[1][i] = WhitePawn(1, i)

    def initializeBlackPawns(self):
        for i in range(8):
            self.board[6][i] = BlackPawn(6, i)

    def printBoard(self):
        printBoard(self.board)

if __name__ == '__main__':
    board = Board()
    board.printBoard()
