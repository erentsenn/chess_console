from Pieces import Piece
def Figure_1List(x, y):
    return [(x, y + 2), (x+1, y + 1), (x - 1, y - 1)]
class Figure_1(Piece):
    def __init__(self, color, name, direction):
        self.name = name
        self.Color = color
        # 1 - идет вперед, -1 - идет назад"
        self.direction = direction

    def availableMoves(self, x, y, gameboard, Color=None):
        if Color is None: Color = self.Color
        answers = []
        if (x + 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x + 1,
                                                                        y + self.direction): answers.append(
            (x + 1, y + self.direction))
        if (x - 1, y + self.direction) in gameboard and self.noConflict(gameboard, Color, x - 1,
                                                                        y + self.direction): answers.append(
            (x - 1, y + self.direction))
        if (x, y + self.direction) not in gameboard and Color == self.Color: answers.append((x,
                                                                                             y + self.direction))
        return answers