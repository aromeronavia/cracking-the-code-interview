from src.board import Board
from src.turn_manager import manageTurn
from src.piece import Piece
from src.empty_coord import EmptyCoord

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
        validateMovement(self, origin)
        self.performMovementIfPossible(origin, destination)

    def validateMovement(self, origin):
        validateOriginIsAPiece(origin)
        validateTurnOfOrigin(origin)

    def validateOriginIsAPiece(self):
        if not isinstance(origin, Piece):
            raise Exception('the origin is not a piece')

    def validateTurnOfOrigin(self):
        if self.turn != origin.color:
            raise Exception('turn of the other color')

    def getPiecesWithCoords(self, x, y):
        return self.board.board[x][y]

    def performMovementIfPossible(self, origin, destination):
        if origin.isMovePossible(destination):
            return self.movePieces(origin, destination)
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
                self.switchTurn()
                self.board.printBoard()
                print 'turn of {0}'.format(self.turn)
            except Exception as error:
                print error
                print 'try the move again!'

    def switchTurn(self):
        self.turn = manageTurn(self.turn)

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
