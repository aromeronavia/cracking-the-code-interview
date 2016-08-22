class Piece(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def canMove(self):
        return

    def isMovePossible(self, destination):
        if isinstance(destination, Piece):
            return self.canEat(destination)
        return self.canMove(destination)

    def canEat(self, origin, destination):
        return self.canMove(origin, destination)

    def isEmpty(destination):
        return destination == ''

    def setNewCoords(self, destination):
        self.x = destination.x
        self.y = destination.y
