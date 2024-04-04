import Board
from colorama import init, Fore
init(autoreset=True)
from Board import Game
WHITE = "white"
BLACK = "black"

game = Game()


def parseInput():
    try:
        a, b = input().split()
        a = ((ord(a[0]) - 97), int(a[1]) - 1)
        b = (ord(b[0]) - 97, int(b[1]) - 1)
        print(a, b)
        return (a, b)
    except:
        print("ошибка при декодировании входных данных. пожалуйста, попробуйте снова")
        return ((-1, -1), (-1, -1))

while True:

    game.printBoard()
    print(game.message)
    game.message = ""
    startpos, endpos = parseInput()
    try:
        target = game.gameboard[startpos]
    except:
        game.message = False  # "На данном месте нет фигуры; координаты вышли за возможный радиус"
        target = None


    if target:
        print("found " + str(target))
        if target.Color != game.playersturn:
            game.message = Fore.BLUE + 'Не ваш ход!'
            continue
        if target.isValid(startpos, endpos, target.Color, game.gameboard):
            game.message = "Хороший ход!"
            game.gameboard[endpos] = game.gameboard[startpos]
            del game.gameboard[startpos]
            game.isCheck()
            if game.playersturn == BLACK:
                game.playersturn = WHITE
            else:
                game.playersturn = BLACK
        else:
            game.message = "Недействительный ход" + str(target.availableMoves(startpos[0], startpos[1], game.gameboard))
            print(target.availableMoves(startpos[0], startpos[1], game.gameboard))
    else:
        game.message = "Здесь нет фигур"


