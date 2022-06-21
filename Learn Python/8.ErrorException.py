
# while 1 print(1) syntax error due to :
# while 1:print(1) # print(1) until we interrrupt

# Exception => Error detected during execution
'''
TYPES =>
ZeroDivisionError
NameError
TypeError and much more
'''

while True:
    try:
        a = input()
        print(a)
    except:
        print("Value not provided")
# infinite time ask for value
