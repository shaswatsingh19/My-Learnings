# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=virtusa

t = int(input())
for i in range(t):
    flag = False
    a=input()
    b =input()
    for j in range(min(len(a),len(b))):
        if a[j] in b:
            print("YES")
            flag = True
            break
    if flag == False:
        print("NO")
