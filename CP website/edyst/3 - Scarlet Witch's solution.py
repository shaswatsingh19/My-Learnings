# https://edyst.com/cohort/daily-coding-challenge-april-2020-0L0oG/module/daily-coding-challenge-april-2020-JxE19/topic/challenge-3-pRMom/question/6/name/-M4YjzNf96wjpyy_5IMI?is_required=1

def seq (h,s):
    l = []
    l.append(h)
    for j in range(s):
        h = 2*h -1
        l.append(h)
    return sum(l)

def password(pwd):
    q = str(pwd)
    alpha = ['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(q)):
        print(alpha[int(q[i])],end = "")
        
        

    
t  = int(input())
for i in range(t):
    time= input()
    time =time.split(":")
    h = int(time[0])
    s = int(time[1])
    pwd = seq(h,s)
    password(pwd)
    print()
