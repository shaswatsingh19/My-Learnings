t = int(input())
for  i in range(t):
    b = int(input())
    ans = 0
    while b > 2:
        ans = ans + (b - 2)//2
        b = b - 2
    print(int(ans))
