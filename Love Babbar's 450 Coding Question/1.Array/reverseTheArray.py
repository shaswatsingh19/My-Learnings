# Problem Statement :- https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

# Solution :-
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


arr = list(map(int,input().split()))
i = 0
j = len(arr)-1
while i<j:
	arr[i],arr[j]  = arr[j],arr[i]
	i+=1
	j-=1
print(arr)
