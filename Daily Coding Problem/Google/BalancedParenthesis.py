# https://workat.tech/problem-solving/practice/balanced-parentheses
import queue as q
class Solution:
	
	def isBalancedParentheses(self, s: str) -> bool:
		# add your logic here
		stack = q.LifoQueue()
		
		for i in s:
			if (i=='}' or i==']' or i==')') and (stack.empty()):
				return 0
			if i =='(' or i=='{' or i == '[':
				stack.put(i)
			elif i==')':
				pop = stack.get()
				if(pop != '('):
					return 0
			elif i==']':
				pop = stack.get()
				if(pop != '['):
					return 0
			elif i=='}':
				pop = stack.get()
				if(pop != '{'):
					return 0
				
		if stack.empty():
			return 1
		return 0
			
			