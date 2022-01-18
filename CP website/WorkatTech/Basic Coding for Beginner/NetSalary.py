# https://workat.tech/problem-solving/practice/net-salary
try:
	t = int(input())
	while(t):
		sal = int(input())
		temp  = sal
		tax =0
		if(temp>0):
			tax  += 0
			temp -= 300000
		# print(tax)

		if(temp>0):
			tax += (min(200000,temp)*5)/100
			temp -= 200000 
		# print(tax)

		if(temp>0):
			tax += (min(500000,temp)*20)/100
			temp -= 500000
		# print(tax)

		if(temp>0):
			tax += (temp*30)/100
		# print(tax)
		net = sal - tax
		print(format(net,".2f"))
			
			
except:
	EOFError