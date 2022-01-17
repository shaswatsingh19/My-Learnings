# Write your code here
# https://workat.tech/problem-solving/practice/candies

try:
	c,co = input().split()
	c = int(c)
	co = int(co)
	if(c%co==0):print("YES")
	else:print("NO")
except:EOFError