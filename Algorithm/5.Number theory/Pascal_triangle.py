# https://workat.tech/problem-solving/practice/pascals-triangle/
class Solution:
	def pascalTriangleRow(self, rowNo: int) -> List[int]:
		# add your logic here
		arr = [0]*rowNo
		rowNo-=1
		arr[0] = 1
	# 		NcR = Nc(R - 1) * (N - R + 1) / R;
		for i in range(1,rowNo+1,1):
			arr[i] = (arr[i-1]*(rowNo-i+1))//i
		return arr


