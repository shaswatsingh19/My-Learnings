# https://workat.tech/problem-solving/practice/vowels
try:
	t = int(input())
	while(t):
		s = input()
		s = s.lower()
		vo = ['a','e','i','o','u']
		cnt = 0
		for i in s:
			for j in vo:
				if(i==j):
					cnt+=1
					break;
		print(cnt)
			
		t-=1
except:EOFError