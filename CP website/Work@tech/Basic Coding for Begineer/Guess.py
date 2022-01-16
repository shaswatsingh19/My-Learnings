# Write your code here
try:
	d = int(input())
	while True:
		g = int(input())
		if(g==d):
			print("Correct Guess")
			break
		else:print("Incorrect Guess")
except:EOFError