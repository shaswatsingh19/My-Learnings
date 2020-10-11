Problem :- https://www.codechef.com/CZEN2020/problems/ALCHHhttps://www.codechef.com/CZEN2020/problems/ALCHH

# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

# # COOEY
try:
        
    s = input()
    cons ={}
    count = 0
    flag  = False
    vowel = ['A','E',"I","O",'U']
    for i in s:
    	if i not in vowel and i not in cons:
    		count = 0
    		cons[i] = 1
    	elif i in vowel :
    		count += 1
    	if count >= 3:
    		flag = True
    
    if flag == True and len(cons) >= 5:
    	print('GOOD')
    else:
    	print(-1)
except:
    EOFError
