# https://edyst.com/cohort/daily-coding-challenge-april-2020-0L0oG/module/daily-coding-challenge-april-2020-JxE19/topic/challenge-5-gV369/question/6/name/-M4Yk1jwI5iReb_evMeY?is_required=1

def iron(n,m):
    dia = list(map(int,input().split()))
    max_dia = max(dia)
    if m < max_dia:
        return "impossible"
    else:
        sum_dia  = sum(dia)
        mini = (sum_dia)//m
        mini = mini  + 1
        return mini
    
        



t = int(input())
while t:
    n,m = input().split()
    n = int(n)
    m = int(m)
    print(iron(n,m))
    t = t - 1
