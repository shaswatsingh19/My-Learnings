#https://leetcode.com/contest/weekly-contest-185/problems/reformat-the-string/
s = input()
num = []
alpha = []
for i in s:
    if i.isalpha() != True:
        num.append(i)
    else:
        alpha.append(i)
if num != []:
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            print("")
elif alpha != []:
    for i in range(len(alpha)-1):
        if alpha[i] ==alpha[i+1]:
            print("")
    
else:
    new = ""
    for i in range(min(len(num),len(alpha))):
        if max(len(num),len(alpha)) == len(alpha):
            new = new + alpha[i]
            new = new +num[i]
        else:
            new  = new+ num[i]
            new = new + alpha[i]
    if len(new) != len(s):
        if max(len(num),len(alpha)) == len(alpha):
            new = new + alpha[len(alpha)-1]
        else:
            new = new + num[len(num) -1]
    
    print(new)
            
