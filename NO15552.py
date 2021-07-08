import sys

count = int(sys.stdin.readline().rstrip())

for _ in range(count):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print(a + b)