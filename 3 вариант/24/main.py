file = open('file.txt')
n = [int(x) for x in file.read()]
file.close()

counter = 1
maxcounter = 1

for i in range(1, len(n)):
    if (n[i] == 2 and n[i-1] == 1) or (n[i] == 1 and n[i-1] == 2):
        counter = 1
    else:
        counter += 1
        maxcounter = max(maxcounter, counter)

print(maxcounter)
