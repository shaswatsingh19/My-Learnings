# Write your code here
# https://workat.tech/problem-solving/practice/adjancent-zeros
try:
	t = int(input())
	while(t):
		n = input()
		check="No"
		for i in range(len(n)-1):
			if(n[i]=='0' and n[i+1]=='0'):
				check  = 'Yes'
				break
		print(check)
			
		
		
		
		t-=1
		
except:
	EOFError