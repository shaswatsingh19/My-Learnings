# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=next-challenge&h_v=zen

n = int(input())
p = list(map(int,input().split()))
q = set(p)
freq = {}
for item in p:
    if item in freq:
        freq[item] = freq[item] + 1
    else:
        freq[item] = 1
for item in p:
    if freq[item] == 1:
        print(item)
