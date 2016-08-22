import unittest
from src.pawn import WhitePawn, BlackPawn
from src.empty_coord import EmptyCoord

class TestWhitePawn(unittest.TestCase):
    def test_creation(self):
        whitePawn = WhitePawn(0, 0)
        self.assertEqual(whitePawn.x, 0)
        self.assertEqual(whitePawn.y, 0)
        self.assertEqual(whitePawn.firstMove, True)
        self.assertEqual(whitePawn.color, 'white')

    def test_first_movement(self):
        # moves one space
        whitePawn = WhitePawn(1, 1)
        canMoveTwo = whitePawn.canMove(EmptyCoord(4, 1))
        self.assertEqual(canMoveTwo, False)
        # moves two spaces
        whitePawn = WhitePawn(1, 1)
        canMoveTwo = whitePawn.canMove(EmptyCoord(2, 1))
        self.assertEqual(canMoveTwo, True)
        # moves three spaces
        whitePawn = WhitePawn(1, 1)
        canMoveTwo = whitePawn.canMove(EmptyCoord(4, 1))
        self.assertEqual(canMoveTwo, False)

    def test_can_eat(self):
        whitePawn = WhitePawn(1, 1)

if __name__ == '__main__':
    unittest.main()
