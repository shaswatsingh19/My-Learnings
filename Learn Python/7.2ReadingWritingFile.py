# open(filename,mode)
"""
mode can be
"w" = write
"r" = read
"r+" = read and write
"""
f = open('workfile','w')


with open('workfile') as f:
    read_data = f.read()

# to check whether file is closed or not
f.closed # False
f.close()
f.closed # True

f.readline() # print next line everytime we run this


# can also use json module to data exchange

'''
json take python code and convert into string => serializing
reconstructing the data from string => deserializing
'''
