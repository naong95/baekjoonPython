n = int(input())

scores = []
scores.append(input().split(" "))

scores = scores[0]
for i in range(n):
    scores[i] = int(scores[i])
m = int(max(scores))

avg = []
for i in range(n):
    avg.append(int(scores[i]))

answer = round(sum(avg) / n / m * 100, 14)
print(answer)