import sys

count = int(sys.stdin.readline().rstrip())

k = 1
for _ in range(count):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    c = str(a + b)

    print("Case #%d: " %k + "%d "%a + "+" " %d = " %b + c)
    k = k + 1