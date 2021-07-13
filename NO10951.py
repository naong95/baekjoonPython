import sys

a = "1"
while True:
    try:
        a, b = sys.stdin.readline().rstrip().split()
        a = int(a)
        b = int(b)
        print(a + b)
    except ValueError:
        break