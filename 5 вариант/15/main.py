def f(A):
    for x in range(1, 1000):
        a = x % A == 0
        b = x % 18 == 0
        c = x % 81 == 0

        if not(a or not b or not c):
            return False

    return True


for A in range(10000, 1, -1):
    if f(A):
        print(A)
        break
