n = int(input())

k = n
for i in range(n):
    k = k - 1
    for i in range(k):
        print(" ", end = '')
    for i in range(n - k):
        print("*", end = '')
    print()