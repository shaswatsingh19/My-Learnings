'''
Alice and Bob are playing a game called "Stone Game". Stone game is a two-player game. Let N be the total number of stones. In each turn, a player can remove either one stone or four stones. The player who picks the last stone, wins. They follow the "Ladies First" norm. Hence Alice is always the one to make the first move. Your task is to find out whether Alice can win, if both play the game optimally.

Input Format:

First line starts with T, which is the number of test cases. Each test case will contain N number of stones.

**Output Format: **

Print "Yes" in the case Alice wins, else print "No".

Constraints:

1<=T<=1000

1<=N<=10000
Sample Input and Output:

3
1
Yes
6
Yes
7
No
'''
# TCS  - Stone Game ( one four)
'''
alice always start first
alice and bob plays optimally
'''
# THIS is a simple method
# method 1

'''
t = int(input())
while t:
    turn = 0 
    n = int(input("Number of stone"))
    while n >= 1:
        if n >=4 :
            n  = n - 4
        else:
            n = n -1
        turn = turn + 1
    if a % 2 ==0:
        print("BOB wins")
    else:
        print("ALICE wins")     
    t = t - 1
'''

# THIS below  is more optimal solution
# with less lines of code

t = int(input())
while t:
    n = int(input("Number of stones\n"))
    moves = int(n / 4) +  (n % 4)
    if (moves % 2) == 0:
        print("BOB Wins")
    else:
        print("ALICE winS")
    t -= 1
