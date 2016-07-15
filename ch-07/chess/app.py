from board import Board
from turn_manager import manageTurn
from piece import Piece
from empty_coord import EmptyCoord

class App:
    def __init__(self, board):
        self.board = board
        self.turn = 'white'

    def getTurn(self):
        return self.turn

    def executeMovement(self, movement):
        (originX, originY, destinationX, destinationY) = self.parseInputMove(movement)
        origin = self.getPiecesWithCoords(originX, originY)
        destination = self.getPiecesWithCoords(destinationX, destinationY)
        if not isinstance(origin, Piece):
            raise Exception('the origin is not a piece')
        if self.turn != origin.color:
            raise Exception('turn of the other color')

        self.performMovementIfPossible(origin, destination)

    def getPiecesWithCoords(self, x, y):
        return self.board.board[x][y]

    def performMovementIfPossible(self, origin, destination):
        if isinstance(destination, Piece):
            if origin.canEat(origin, destination):
                self.movePieces(origin, destination)
            else:
                raise Exception('cant move to destination')
        else:
            if origin.canMove(destination):
                self.movePieces(origin, destination)
            else:
                raise Exception('cant move to destination')

    def movePieces(self, origin, destination):
        self.board.board[destination.x][destination.y] = origin
        self.board.board[origin.x][origin.y] = EmptyCoord(origin.x, origin.y)
        origin.x = destination.x
        origin.y = destination.y

    def run(self):
        self.board.printBoard()
        while(True):
            movement = raw_input('Move')
            try:
                self.executeMovement(movement)
                self.turn = manageTurn(self.turn)
                self.board.printBoard()
                print 'turn of {0}'.format(self.turn)
            except Exception as error:
                print error
                print 'try the move again!'

    def getColumnIndexByCharacter(self, character):
        return ord(character) - 97

    def parseInputMove(self, movement):
        (originCoords, destinationCoords) = movement.split('-')
        originX = self.getColumnIndexByCharacter(originCoords[0])
        originY = int(originCoords[1])
        destinationX = self.getColumnIndexByCharacter(destinationCoords[0])
        destinationY = int(destinationCoords[1])
        return (originX, originY, destinationX, destinationY)

app = App(Board())
app.run()
