print('hello ') # single quotes 
print("hello ") # double quotes

print( " \"Doesn\'t\" ") # use \ before quotes to act as aquote

print(' First line \n second line') # \n line seperater


print(r'First \n second') # use r before quote to treat as normal character with no power


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

b = 'b'
a = 'a'
print("b"+"an"*2 +"a") # multiple string by number of times
print(b+"an"*2 +a) 

text = ('Put several strings within parentheses '
           'to have them joined together.')

print(text)

word  = 'python'

# INDEXING (to obtain characters)
print(word[0]) # p
print(word[3]) # h
print(word[-1]) # n -1 means last
print(word[-3]) # h third last

#SLICING (to obtain substring)
print(word[0:]) # printall from 0 to end
print(word[0:3]) # first three charcter combined to form new string
print(word[-3:-5]) # start from third last to 5 last 
print(word[-2:]) # second last to all

print (word[:2] + word[2:])

print(word[4:400]) # the word length is 6 but it will consider
print(word[4:]) # this is same as above

# word[0] = 'A'
#not allowed as string are immutable
# we can make new string but can't change string

print(len(word)) # build in len() function 
