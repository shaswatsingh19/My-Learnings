'''
PROBLEM :

        link : https://www.hackerearth.com/problem/algorithm/apna-bhai-kon-gaitonde/description/

        Faizal decided to contest Lok Sabha elections. So instead of wasting time in lockdown, he decided to devise an algorithm (Faizal ko bhi pata hai algorithm kya hoti h, aap usko mat sikhaayiye) so that he can get maximum votes.

        After the election, it was very hard to decide and count votes by hands as there was no EVM at the time of Faizal. So, the Election Commissioner decided to devise an algorithm that can decide who won the election.

        But there is a mistake in the algorithm they have made an algorithm that only decides a winner if the number of votes in favor of one candidate is more than half of the total number of votes, i.e. greater than .

        Your goal is to devise the same algorithm that the election commission has devised and it must run in O(n log n) or less.

        Problem Description:

        Task:

        The goal of this code problem is to check whether an input sequence contains a majority element, i.e. count of an element in the array is greater than half of the total number of elements.

        (Faizal ko chodhho bhai, use algorithm banana mat sikhaao. Katte se zyada waise hi nahi hota kuch unme!)

        Input Format:

        The first line contains , the number of test cases. For each test case,

        the first line contains an integer  and the next one contains a sequence of  non-negative integers .

        Constraints:




        Output Format:

        For each test case output 1 if the sequence contains an element that appears strictly more than  times 0 otherwise separated by next line.

        Example:

        Input: 

        1
        5
        2 3 9 2 2
        Output: 

        1
        Explanation: Because 2 is the majority element.
'''

# SOLUTION :


        t = int(input())
        while t :
            n  = int(input())
            ar = list(map(int,input().split()))
            c = 0
            el = 0
            for i in ar:
                if c == 0:
                    el = i
                if el == i:
                    c += 1
                else:
                    c -= 1
            count = ar.count(el)
            if count > n/2:
                print(1)
            else:
                print(0)
            t = t -1
