n = int(input())
scores = []
score = []
for i in range(n):
    scores.append(input().split(" "))

for i in range(n):
    score = scores[i][1:]
    score = list(map(int, score))

    avg = sum(score) / len(score)
    count = 0
    for s in score:
        if(s > avg):
            count = count + 1
    print(str(round(count / len(score) * 100, 3)) + "%")