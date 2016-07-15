#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from piece import Piece

class Pawn(Piece):
    def __init__(self, x, y, color):
        self.firstMove = True
        super(Pawn, self).__init__(x, y, color)

    def canMove(self, destination):
        if self.firstMove:
            if abs(destination.y - self.y) != 2:
                return False
            return True
        else:
            if abs(destination.y - self.y) != 1:
                return False
            return True

    def canEat(self, destination):
        return

    def __repr__(self):
        if (self.color == 'black'):
            return '♙'
        return '♟'
