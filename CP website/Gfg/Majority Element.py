Question : https://practice.geeksforgeeks.org/problems/majority-element/0
	Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

	Input:  
	The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

	Output: 
	For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

	Constraints:
	1 <= T<= 100
	1 <= N <= 107
	0 <= Ai <= 106

	Example:
	Input:
	2
	5
	3 1 3 3 2
	3
	1 2 3

	Output:
	3
	-1

	Explanation:
	Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.


	** For More Input/Output Examples Use 'Expected Output' option **

Solution :
	t = int(input())
	while t:
		n = int(input())
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
			print(el)
		else:
			print(-1)
		t = t- 1
