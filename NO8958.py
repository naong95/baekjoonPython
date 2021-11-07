n = int(input())
oxes = []
a = []
l = []

for i in range(n):
    oxes.append(input().split(" "))

for i in range(n):
    a.append(oxes[i][0])


for i in range(n):
    l.append(len(a[i]))
    score = 0
    count = 0
    for k in range(l[i]):
        if(a[i][k] == "O"):
            count = count + 1
            if(k == l[i] - 1):
                score = score + (count * (count + 1) / 2)
        else:
            score = score + (count * (count + 1) / 2)
            count = 0
    print(int(score))