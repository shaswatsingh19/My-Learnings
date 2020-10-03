'''
PROBLEM : 
        Link : https://www.interviewbit.com/problems/spiral-order-matrix-i/
        Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

        Example:

        Given the following matrix:

        [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        You should return

        [1, 2, 3, 6, 9, 8, 7, 4, 5]

SOLUTION :
'''
        class Solution:
            # @param A : tuple of list of integers
            # @return a list of integers
            def spiralOrder(self, A):

                row = len(A)
                mat =[]
                col = len(A[0])
                t = 0
                b = row - 1
                l = 0
                r = col -1
                d  =0
                while (t <= b and l<=r):
                    if d == 0:
                        for i in range(l,r+1):
                            mat.append(A[t][i])
                        t += 1
                        d =1
                    elif d == 1:
                        for i in range(t,b+1):
                            mat.append(A[i][r])
                        r -= 1
                        d = 2
                    elif d== 2:
                        for i in range(r,l-1,-1):
                            mat.append(A[b][i])
                        b -= 1
                        d = 3
                    elif d==3:
                        for i in range(b,t-1,-1):
                            mat.append(A[i][l])
                        l += 1
                        d = 0
                return mat

