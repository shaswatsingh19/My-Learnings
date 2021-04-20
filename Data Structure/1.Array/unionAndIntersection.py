'''
Find union and intersection of an array
'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# Method 1 : Naive approach using set() and its prebuild function
# set1.union(set2) and set1.intersection(set2)

t = int(input())
while t:
	a,b=map(int,input().split())
	arr = list(map(int,input().split()))
	brr = list(map(int,input().split()))
	arr=set(arr)
	brr=set(brr)
	print(arr.union(brr))
	print(arr.intersection(brr))
	t-=1


# Method 2: Searching and sorting
print("METHOD 2 for union")

def binary(ar,x,l,h):
    while l<=h:
        m = (l+h)//2
        if arr[m]==x:
            return True
        elif arr[m]<x:
            return binary(ar,x,m+1,h)
        else:
            return binary(ar,x,l,m-1)
    return False
t = int(input())
while t:
    a,b=map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    u =[]
    la  = len(arr)
    lb =len(brr)
    if la>=lb:
        brr = sorted(brr)
        u.extend(brr)        
        for i in range(la):
            x = arr[i]
            if binary(brr,x,0,lb-1):
                continue
            else:
                u.append(x)
    print(u)
    t-=1

'''

'''