QUESTION:

        link: https://www.spoj.com/problems/MAJOR/
        The human tribe has just discovered some other tribe and wants to communicate with them. To make sure it is not intercepted by the terminators, they ask their chief computer engineer Rohit to design a system for the purpose. In the design that Rohit proposes, data is transmitted n times. If it is received more than half-the times, it is said to be successfully transmitted. If not, the data is said to be lost. Rohit obviously got a lot of fame and respect for his work. Nitish doesn’t like it and wants to challenge Rohit’s supremacy. He wants to check out the system and has hired you for the process.

        Input
        The first line of the input contains test cases t (1 <= t <= 100). It is followed by 2*t lines, 2 for each test case. The first line of input for each test case contains a number n (0 <= n <= 106), followed by n elements in the next line. Each number is from -10^3 to +10^3

        Output
        You are required to output ‘YES’ followed by the number transmitted, if it was transmitted successfully, and ‘NO’ otherwise.

        Example
        Input:
        3
        4
        2 1 2 2
        6
        1 1 1 2 2 2
        5
        1 2 4 5 1

        Output:
        YES 2
        NO
        NO

SOLUTION:

        t = int(input())
        while t:
          n = int(input())
          ar = list(map(int,input().split()))
          c = 0
          el = 0
          for i in ar:
            if c==0:
              el = i
            if el == i:
              c += 1
            else:
              c -= 1
          if ar.count(el) > n/2:
            print('YES '+str(el))		
          else:
            print('NO')
          t = t-1
