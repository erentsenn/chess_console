
from Pieces import Piece
def knightList(x, y, int1, int2):
    """специально для ладьи переставляет значения, необходимые для определения позиции для неконфликтных тестов"""
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]
class Knight(Piece):
    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        return [(xx, yy) for xx, yy in knightList(x, y, 2, 1) if self.noConflict(gameboard, Color, xx, yy)]

