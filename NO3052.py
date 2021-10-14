lines = []

for line in range(10):
    line = int(input()) % 42
    lines.append(line)

answer = len(set(lines))
print(answer)