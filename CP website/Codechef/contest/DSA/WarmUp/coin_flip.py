    # https://www.codechef.com/LRNDSA01/problems/CONFLIP
'''
try:
    t = int(input())
    for  i in range(t):
        g = int(input())
        for i in range(g):
            # i = 1 = head and i = 2 = tail
            #n = no of rounds
            # q = what to find i.e q = 1 means find head else tail
            i,n,q = map(int,input().split())
            if i == 1:
                a = ['H']*n
            else :
                a = ['T']*n
            tail_count = 0
            head_count = 0
            for i in range(n):
                if (n-i)%2 ==0:
                    a[i] = 'H'
                    head_count += 1
                else:
                    a[ i] = 'T'
                    tail_count += 1
            if q == 1:
                print(head_count)
            elif q == 2 :
                print(tail_count)

except:
        EOFError
'''

'''
t = int(input())
for i in range(t):
    g = int(input())
    for j in range(g):
        i,n,q = map(int,input().split())
        if (not n%2) or i == q:
            print(n >> 1)
            continue
        print((n>>1) + 1)
'''

t = int(input())
for i in range(t):
    g = int(input())
    for _ in range(g):
        i,n,q = map(int,input().split())
        if i == q:
            print(n//2)
        else:
            print(n - n//2)

