def base(n):
    if n<9:
        return n
    else:
        return n%9 + 10*base(n//9)

while True:
    try:
        n = int(input())
        print(base(n))
    except:
        EOFError
        break