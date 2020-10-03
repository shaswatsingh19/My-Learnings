# https://edyst.com/cohort/daily-coding-challenge-april-2020-0L0oG/module/daily-coding-challenge-april-2020-JxE19/topic/challenge-2-Yq97Y/question/6/name/-M4Yjxoetp52EOpJjDMA?is_required=1

t =int(input())
while t:
    n,p = map(int,input().split())
    l = [0] * n
    temp = p
    for i in range(n):
        for j in range(i,n):
            if temp == 0:
                break
            l[j]= l[j] + 1
            temp = temp - 1
          
    diff  = p - sum(l)
    if diff > 0 :
        l[0]  = l[0] + diff 
    for i in range(n):
        print(l[i],end= " ")
    print()
    t = t- 1
    
