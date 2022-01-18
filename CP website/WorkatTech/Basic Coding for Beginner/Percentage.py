# Write your code here
# https://workat.tech/problem-solving/practice/percentage
try:
	n = int(input())
	avg= 0
	while(n):
		mark = int(input())
		avg += mark
		# print(avg)
		n-=1
	avg = (avg)/5
	avg = avg*100
	avg = avg/80
	# avg = "%.2f"%avg
	# print((str(avg)+"%").rstrip(' '))
	print(format(avg,".2f")+'%')

	
except:EOFError