class Piece(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def canMove(self):
        return

    def canEat(self, origin, destination):
        return self.canMove(origin, destination)

    def isEmpty(destination):
        return destination == ''
