import sys

n = int(sys.stdin.readline().rstrip())
a = []
a = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(a), max(a))