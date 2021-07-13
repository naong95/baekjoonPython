import sys

n, x = sys.stdin.readline().rstrip().split()

x = int(x)

a = []
a = sys.stdin.readline().rstrip().split()
a = list(map(int, a))

k = 0
for i in a:
    if(a[k] < x):
        print(i, end = ' ')
    k = k + 1
