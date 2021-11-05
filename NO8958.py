n = int(input())
oxes = []
a = []
l = []

for i in range(n):
    oxes.append(input().split(" "))

for i in range(n):
    a.append(oxes[i][0])

score = 0
for i in range(n):
    l.append(len(a[i]))

    for k in range(l[i] - 1):
        if(a[k] == "O"):
            score = score + 1
            if(a[k + 1] == "O"):
                score = score + 1
        else:
            score = score + 0

print(score)