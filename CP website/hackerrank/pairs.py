# https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=virtusa

n,k = map(int,input().split())
a = list(map(int,input().split()))
count = 0
a.sort()
j = 1
i = 0
while j<n:
    diff = abs(a[j] -a[i])
    if diff == k:
        count = count  + 1
        j = j + 1
    elif diff > k:
        i = i + 1
    elif diff < k:
        j = j + 1
        
    
