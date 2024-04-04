from Pieces import Piece
from Pieces import chessCardinals
class Rook(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)
