# https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    first = []
    for i in s:
        first.append(ord(i))

    f = 0
    l = len(first)-1
    while f<l:
        if abs(first[f]-first[f+1]) != abs(first[l] - first[l-1]):
            return "Not Funny"
        f = f+1 
        l = l-1 
    return "Funny"
	
q = int(input())
for _ in range(q):
	s = input()
	result  = funnyString(s)
	print(result)
