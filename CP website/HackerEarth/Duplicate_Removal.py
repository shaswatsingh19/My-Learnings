PROBLEM LINK: https://www.hackerearth.com/problem/algorithm/duplicate-removal-3/

PROBLEM STATEMENT :
Remove the duplicate elements from an array

SAMPLE INPUT 
1	2	3	2	10
SAMPLE OUTPUT 
1	2	3	10
Explanation
Input: 1 2 3 2 10 Output: 1 2 3 10

Remove duplicate elements and print the array spaced by '\t' character.

Time Limit:	5.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB


sOLUTION :

a=[int(x) for x in input().split()]

output=[]
for x in a:
        if x not in output:
                output.append(x)
for i in range(len(output)-1):
        print(output[i], end='\t')
print(output[-1])
