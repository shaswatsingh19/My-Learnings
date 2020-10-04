When one number is divided by another, the modulo operation finds the remainder. It is denoted by the  symbol.

Example

Assume that you have two numbers 5 and 2.  is 1 because when 5 is divided by 2, the remainder is 1.

Properties
    1.(a+b)%c = ((a%c)+(b%c)%c)
    2.(a*b)%c = ((a%c)*(b%c)%c)
    3.(a-b)%c = ((a%c)-(b%c)+c)%c
    4.(a/b)%c = ((a%c)*(b(-1)%c)%c)

Note: In the last property,  is the multiplicative modulo inverse of b and c.

Very useful while calculating very big number like 10**18 
