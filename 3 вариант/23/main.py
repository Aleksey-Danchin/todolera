def f(a, b):
    if a == b:
        return 1

    if a > b:
        return 0

    return f(a + 2, b) + f(a + 10, b)


for i in range(6, 142):
    print(i, f(5, i))

# arr = []
# for i in range(142):
#     arr.append(0)

# arr[5] = 1

# for i in range(5, 142):
#     if i + 2 < 142:
#         arr[i + 2] += arr[i]
#     if i + 10 < 142:
#         arr[i + 10] += arr[i]

# print(arr[141])
