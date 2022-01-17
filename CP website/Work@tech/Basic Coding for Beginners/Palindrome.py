# Write your code here
# https://workat.tech/problem-solving/practice/palindrome
try:
	t = int(input())
	while(t):
		s = input()
		i=0
		j=len(s)-1
		check = True
		while(i<j):
			if(s[i]!=s[j]):
				check=False
				break
			i+=1
			j-=1
		print(check)
		t-=1
except:
	EOFError