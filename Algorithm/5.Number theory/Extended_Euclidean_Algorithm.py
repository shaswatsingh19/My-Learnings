'''
While the Euclidean algorithm calculates only the greatest common divisor (GCD) of two integers a and b
the extended version also finds a way to represent GCD in terms of a and b
i.e. coefficients x and y for which:
                (a⋅x)+ (b⋅y) = gcd(a,b)
'''
# Python program to demonstrate working of extended 
# Euclidean Algorithm  from gfg
	
# function for extended Euclidean Algorithm 
def gcdExtended(a, b): 

	# Base Case 
	if a == 0 : 
		return b, 0, 1
			
	gcd, x1, y1 = gcdExtended(b%a, a) 
	
	# Update x and y using results of recursive 
	# call 
	x = y1 - (b//a) * x1 
	y = x1 
	
	return gcd, x, y 
	

# Driver code 
a, b = 15, 5
g, x, y = gcdExtended(a, b) 
print("gcd(", a , "," , b, ") = ", g) 
print('(',a,'*',x,') + (',b,'*',y,') =',g)


	

