# https://edyst.com/cohort/daily-coding-challenge-april-2020-0L0oG/module/daily-coding-challenge-april-2020-JxE19/topic/challenge-4-v9l78/question/6/name/-M4Yk-mFMPzgR1Tyx34M?is_required=
def grid(titan,n):
    # row
    i = 0
    c = n[0]
    r_count = 0
    c_count = 0
    count = 
    while i < pow(n[0],n[0]):
        if len(set(titan[i:n[0]])) != len(set(titan[n[0]:n[0]+c])):
            r_count = r_count + 1
        i = i + c
        n[0] = n[0] + c
# column


t = int(input())
for  i in range(t):
    m  = list(map(int,input().split()))
    n = m[0:2]
    titan = m[2:]
    grid(titan,n)
