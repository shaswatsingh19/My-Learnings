Problem  :- https://codeforces.com/contest/770/problem/A


# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


a,b =map(int,input().split())
ans = ''
for i in range(b):
	ans += chr(i+97)

ans = ans*a
print(ans[:a])


 
