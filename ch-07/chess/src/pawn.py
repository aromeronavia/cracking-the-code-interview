#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from piece import Piece

class WhitePawn(Piece):
    def __init__(self, x, y):
        self.firstMove = True
        color = 'white'
        super(WhitePawn, self).__init__(x, y, color)


    def canEat(self, destination):
        if (self.x - destination.x != 1
                and self.y - destination.y != 1):
            return False
        return True

    def canMove(self, destination):
        if self.firstMove:
            if destination.x - self.x > 2:
                return False

            self.firstMove = False
            return True
        else:
            if destination.x - self.x != 1:
                return False
            return True

    def canEat(self, destination):
        return

    def __repr__(self):
        return '♟'

class BlackPawn(Piece):
    def __init__(self, x, y):
        self.firstMove = True
        color = 'black'
        super(BlackPawn, self).__init__(x, y, color)

    def canEat(self, destination):
        return

    def canMove(self, destination):
        if self.firstMove:
            if self.x - destination.x > 2:
                return False

            self.firstMove = False
            return True
        else:
            if self.x - destination.x != 1:
                return False
            return True

    def canEat(self, destination):
        return

    def __repr__(self):
        return '♙'
