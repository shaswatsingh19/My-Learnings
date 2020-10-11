# https://www.codechef.com/LRNDSA01/problems/LAPIN
try:
    t = int(input())
    for  i in range(t):
        s = input()
        half = len(s)//2
        if len(s) % 2==0:
            if sorted(s[:half]) == sorted(s[half:]):print("YES")
        else:
            print("NO")
        else:
            if sorted(s[:half]) == sorted(s[half + 1:]):
                print("YES")
            else:
                print("NO")

except:
    EOFError
