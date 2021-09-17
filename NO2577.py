t = 1

for m in range(3):
    m = int(input())
    t = t * m

word = []
word = str(t)


a, b, c, d, e, f, g, h, i, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

k = 0
indexes = []
for _ in range(len(word)):
    indexes.append(k)
    k = k + 1

for index in indexes:
    if(word[index] == '0'):
        a = a + 1
    elif(word[index] == '1'):
        b = b + 1
    elif(word[index] == '2'):
        c = c + 1
    elif(word[index] == '3'):
        d = d + 1
    elif(word[index] == '4'):
        e = e + 1
    elif(word[index] == '5'):
        f = f + 1
    elif(word[index] == '6'):
        g = g + 1
    elif(word[index] == '7'):
        h = h + 1
    elif(word[index] == '8'):
        i = i + 1
    elif(word[index] == '9'):
        j = j + 1

print(a, b, c, d, e, f, g, h, i, j)