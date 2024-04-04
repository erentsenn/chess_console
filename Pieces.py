chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

class Piece:
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color

    def isValid(self, startpos, endpos, Color, gameboard):
        if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color=Color):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def availableMoves(self, x, y, gameboard):
        print("ОШИБКА")

    def AdNauseum(self, x, y, gameboard, Color, intervals):
        """повторяет заданный интервал до тех пор, пока не появится другая фигура.
        если эта фигура не того же цвета, этот квадрат добавляется, а
        затем возвращается список"""
        answers = []
        for xint, yint in intervals:
            xtemp, ytemp = x + xint, y + yint
            while self.isInBounds(xtemp, ytemp):
                # print(str((xtemp,ytemp))+"is in bounds")

                target = gameboard.get((xtemp, ytemp), None)
                if target is None:
                    answers.append((xtemp, ytemp))
                elif target.Color != Color:
                    answers.append((xtemp, ytemp))
                    break
                else:
                    break

                xtemp, ytemp = xtemp + xint, ytemp + yint
        return answers

    def isInBounds(self, x, y):
        "проверка, не вышли ли за координаты доски"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def noConflict(self, gameboard, initialColor, x, y):
        "проверка неконфликтности позиций"
        if self.isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor):
            return True
        return False
