# 
def hello():
    print("hello")
hello()
print("–------------------------------")

# single variable
def hello(n1):
    print(n1)
hello(26)
print("---–----------------------------")

# list
def arr(list):
    print(list)
arr([3,5,6,'h4lo'])
print("----------------------------------")

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

#
def student(username , password , email):
    print(student) 
#
def keyword_arguments(name,age):
    print(name)
    print(age)

# keyword_arguments(39,'azhar') 
keyword_arguments( age=33 , name = 'hamza') # keyword arguments 'age' , 'name' etc 

# Que 1 -  take unknown no of numbers as parameters and get sum of all numbers(parameters)
# add(2,4,5,6,0,7,8,8)

# Que2 - username,password,email
username = input("enter your name :") # their is 3 letter in the name
password = input("enter a password :") # 8 no. of character 
email = input("enter a email :") # @ not present it is not valid
