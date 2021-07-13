import sys

a = "1"
b = "1"

while True:
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    if a + b == 0:
        break
    print(a + b)