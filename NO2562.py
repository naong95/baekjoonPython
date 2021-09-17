lines = []

for line in range(9):
    line = int(input())
    lines.append(line)

m = max(lines)
i = lines.index(m)

print(m)
print(i + 1)