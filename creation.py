from arhitecture import Cell, Town, Resources
from random import randrange


def field_creation():
    global result
    # потенциальное расширение на поле с регулируемым кол вом ячеек
    # так же необходимо дополнить поле "рандомайзером ячеек"
    total = {'Town': 6, 'Resources': 28}
    result = [[Cell() for j in range(11)] for i in range(11)]
    for _ in range(28):
        i = randrange(11)
        j = randrange(11)
        while type(result[i][j]) == type(Resources):
            i = randrange(11)
            j = randrange(11)
        result[i][j] = Resources()
    for _ in range(6):
        i = randrange(1, 10)
        j = randrange(1, 10)
        while chek(i, j):
            i = randrange(1, 10)
            j = randrange(1, 10)
        result[i][j] = Town()
    return result
    # вернуть двухмерный список обьктов класса Cell, Town, Resources


def chek(i, j):
    if type(Town()) in list(
            map(lambda x: type(x),
                result[i][j - 1: j + 2] + result[i + 1][j - 1: j + 2] + result[i - 1][j - 1: j + 2])):
        return True
    tot = []
    j_min = 1
    j_max = 2
    if j > 2:
        j_min = 2
    if j < 9:
        j_max = 3
    tot += result[i][j - j_min: j + j_max] + result[i + 1][j - j_min: j + j_max] + result[i - 1][j - j_min: j + j_max]
    if i > 1:
        tot += result[i - 2][j - j_min: j + j_max]
    if i < 9:
        tot += result[i + 2][j - j_min: j + j_max]
    if type(Town()) in list(map(lambda x: type(x), tot)):
        return True
    return False
