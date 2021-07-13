n = int(input())
if(n < 10):
    n = n * 10
k = n

i = 0
while True:
    a = k / 10
    a = int(a)
    
    b = k % 10
    b = int(b)
    
    if(a + b < 10):
        k = (b * 10) + a + b
    else:
        k = (b * 10) + ((a + b)%10)

    i = i + 1
    if(k == n):
        break

print(i)
