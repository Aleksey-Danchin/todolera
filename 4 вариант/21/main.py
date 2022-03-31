def game(s, turn=0):
    if s >= 2022:
        return turn in (2, 4)

    if turn >= 4:
        return False

    if turn % 2 == 0:
        return game(s + 1, turn + 1) and game(s * 2, turn + 1)

    return game(s + 1, turn + 1) or game(s * 2, turn + 1)


for s in range(1, 2021):
    if game(s):
        print(s)
