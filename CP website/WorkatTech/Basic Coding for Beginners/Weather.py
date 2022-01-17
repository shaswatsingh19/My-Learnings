# Write your code here
try:
	a = int(input())
	while(a):
		t,h = input().split(" ")
		t  = int(t)
		h  = int(h)
		if(t>=30 and h>=90):print('Hot and Humid')
		elif(t>=30 and h<90):print('Hot')
		elif(t<30 and h>=90):print('Cool and Humid')
		else:print('Cool')
		a-=1
except:
	EOFError