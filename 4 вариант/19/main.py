def game(s, turn=0):
    if s >= 2022:
        return turn == 2

    if turn >= 2:
        return False

    if turn % 2 == 0:
        return game(s + 1, turn + 1) and game(s * 2, turn + 1)

    return game(s + 1, turn + 1) or game(s * 2, turn + 1)


for s in range(1, 2021):
    if game(s):
        print(s)
        break
