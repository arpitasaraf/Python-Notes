# 
def hello():
    print("hello")
hello()

# single variable
def hello(n1):
    print(n1)
hello(26)

# list
def arr(list):
    print(list)
arr([3,5,6,'h4lo'])

# 
def arr(list):
    print(list)
    for i in list:
        print(i)
    
arr([2,4,6,8,10])

## ##  *args used to pass unknown number of arguments to a function
def multiple_args(*args):
    # print(args)
    # for element in args:
    #     print(element)
    pass 
multiple_args(1,'hello',10000 , True , False)

# Que 1 -  take unknown no of numbers as parameters and get sum of all numbers(parameters)
# add(2,4,5,6,0,7,8,8)

def keyword_arguments(name,age):
    print(name)
    print(age)

# keyword_arguments(39,'azhar') 
keyword_arguments( age=33 , name = 'hamza') # keyword arguments 'age' , 'name' etc 
