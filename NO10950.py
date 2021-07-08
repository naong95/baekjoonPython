count = input().split()
count = int(count[0])

N = [input() for _ in range(count)]
N = list(map(tuple, N))

plus =[]
for i in range(count):
    result = int(N[i][0]) + int(N[i][2])
    plus.append(result)

for i in plus:
    print(i)
