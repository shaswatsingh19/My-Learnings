# https://workat.tech/problem-solving/practice/toggle-case
# Write your code here
try:
	t = int(input())
	while(t):
		s = input()
		l = list(s)
		for i in range(len(l)):
			if(l[i].islower()):
				l[i] = l[i].upper()
			else:
				l[i] = l[i].lower()
		print("".join(l))
		t-=1
except:EOFError