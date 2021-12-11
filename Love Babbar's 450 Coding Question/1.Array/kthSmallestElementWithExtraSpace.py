'''
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. 
It is given that all array elements are distinct.

Input:
The first line of input contains an integer T, denoting the number of testcases.
Then T test cases follow. 
Each test case consists of three lines. 
First line of each testcase contains an integer N denoting size of the array.
Second line contains N space separated integer denoting elements of the array.
Third line of the test case contains an integer K.

Output:
Corresponding to each test case, print the kth smallest element in a new line.
'''#code
t = int(input())
while t:
    n = int(input())
    arr = list(map(int,input().split()))
    k =int(input())

    
    b = []
    # Take an extra space and insert element until its lenght equal
    # to k and then remove the max element
    # at last print the max element
    for i in range(n):
        b.append(arr[i])
        if len(b)>k:
            b.remove(max(b))
            
    print(max(b))
    t-=1
    
'''
For Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4
your output is: 
7
15

'''
