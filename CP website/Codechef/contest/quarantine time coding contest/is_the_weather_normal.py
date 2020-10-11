# https://www.codechef.com/QTCC2020/problems/VIEW2005

t = int(input())
while t:
    ah ,al ,nh ,nl = map(int,input().split())
    diff_h = ah - nh
    diff_l = al - nl
    avg = (diff_h + diff_l)/2
    if avg < 0:
        print(str(abs(avg))+" DEGREE(S) BELOW NORMAL")
    else:
           print(str(abs(avg))+" DEGREE(S) ABOVE NORMAL")   
    t= t -1
