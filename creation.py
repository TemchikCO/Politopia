from arhitecture import Cell, Town, Resources
from random import randrange


def field_creation():
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
        while type(Town()) in list(map(lambda x: type(x), result[i][j - 1: j + 2] + result[i + 1][j - 1: j + 2] + result[i - 1][j - 1: j + 2])):
            # print(result[i - 1:i + 1][j - 1: j + 1][0], sep='\n')
            i = randrange(1, 10)
            j = randrange(1, 10)
        result[i][j] = Town()
    return result
    # вернуть двухмерный список обьктов класса Cell, Town, Resources

