counter = 0

for i in range(100, 1000):
    a = ''

    while i > 0:
        a = str(i % 4) + a
        i = i // 4

    a = [int(x) for x in list(a)]

    flag = True

    for i in range(1, len(a)):
        if a[i - 1] < a[i]:
            flag = False
            break

    if flag:
        counter += 1

print(counter)
