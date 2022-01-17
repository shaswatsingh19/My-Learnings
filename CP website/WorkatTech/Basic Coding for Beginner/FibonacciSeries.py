# https://workat.tech/problem-solving/practice/fibonacci-series

try:
	t = int(input())
	while(t):
		n = int(input())
		f = 0
		ans = ''
		s = 1
		if(n<2):
			ans = str(f)
		else:
			ans = str(f)+" "+str(s)+" "
			for i in range(2,n):
				temp = s
				s = f+s
				ans += str(s)+" "
				f = temp
			
		
		print(ans.rstrip())
		t-=1
		
except:EOFError