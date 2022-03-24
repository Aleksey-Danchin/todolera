n = 800000
s = 5

while s > 0 and n > 0:
    n -= 1

    for minDivider in range(2, n):
        if n % minDivider == 0:
            break

    for maxDivider in range(n - 1, 1, -1):
        if n % maxDivider == 0:
            break

    if maxDivider > minDivider:
        diff = maxDivider - minDivider

        if diff % 17 == 0:
            s -= 1
            print(n, diff)
