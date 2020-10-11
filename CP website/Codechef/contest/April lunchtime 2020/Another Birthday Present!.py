# https://www.codechef.com/LTIME83B/problems/SHUFFLE
def sequence(n,k):
    a = list(map(int,input().split()))
    b = sorted(a)
    maxi = a[0]
    for i in range(n-1):
        if a[i+1] > maxi:
            maxi = a[i+1]
        elif a[i+1] < maxi:
            temp = a[i]
            a[i] = a[i+k]
            a[i+k] = temp
    if a == b:
        return "yes"
    else:
        return "no"

        
            

t = int(input())
while t:
    n,k = input().split()
    n = int(n)
    k  =int(k)
    print(sequence(n,k))
    t  = t  -1 
