import itertools
from Pieces import Piece
from Knight import Knight
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from King import King
from Pawns import Pawn
from settings import *


class Game:
    def __init__(self):
        self.playersturn = BLACK
        self.uniDict = {WHITE: {Pawn: "p", Rook: "r", Knight: "h", Bishop: "b", King: "k", Queen: "q"},
                        BLACK: {Pawn: "P", Rook: "R", Knight: "H", Bishop: "B", King: "K", Queen: "Q"}}
        self.message = "Ход белых (внизу)"
        self.gameboard = {}
        self.placePieces()

    def placePieces(self):
        for i in range(0, 8):
            self.gameboard[(i, 1)] = Pawn(WHITE, self.uniDict[WHITE][Pawn], 1)
            self.gameboard[(i, 6)] = Pawn(BLACK, self.uniDict[BLACK][Pawn], -1)

        placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(0, 8):
            self.gameboard[(i, 0)] = placers[i](WHITE, self.uniDict[WHITE][placers[i]])
            self.gameboard[((7 - i), 7)] = placers[i](BLACK, self.uniDict[BLACK][placers[i]])
        placers.reverse()

    def isCheck(self):
        king = King
        kingDict = {}
        pieceDict = {BLACK: [], WHITE: []}
        for position, piece in self.gameboard.items():
            if type(piece) == King:
                kingDict[piece.Color] = position
            print(piece)
            pieceDict[piece.Color].append((piece, position))
        # белые

    def canSeeKing(self, kingpos, piecelist):
        # проверка, может ли хоть какая то фигура в piece list (which is an array of (piece,position) tuples) видеть king в kingpos
        for piece, position in piecelist:
            if piece.isValid(position, kingpos, piece.Color, self.gameboard):
                return True

    def printBoard(self):
        if self.playersturn == BLACK:
            pass
        else:
            pass
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print('   ', *letters, '   ', '\n' '-----------------------')
        for i in range(0, 8):
            print(chr(i + 49), "|", end=" ")
            for j in range(0, 8):
                item = self.gameboard.get((j, i), ".")
                print(str(item), end=" ")
            print("|", chr(i + 49), end=" ")
            print()
        print('-----------------------', '\n', '  ', *letters, '   ')
