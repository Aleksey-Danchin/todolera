def f(n):
    n -= n % 4
    m = []

    while n > 0:
        m.append(n % 2)
        n = n // 2

    m = m[::-1]

    for _ in range(2):
        s = sum(m)
        m.append(s % 2)

    r = 0

    for i in range(len(m)):
        r += m[-i-1] * 2 ** (i)

    return r


arr = [f(x) for x in range(1_000)]
arr = [x for x in arr if x > 56]
print(min(arr))
