# 1) Arithmatic operators
a = 12 
b = 6
# addition
print(a+b)
# subtraction
print(a-b)
# multiple
print(a*b)
# division
print(a/b)
# modules
print(a%b)
# exponnent
print(a**b)
# floor division
print(a//b)

# 2) Comparison 
c = 10
d = 5
# equal to equal
print(c==d)
# not equal
e = 5!=5
print(e)
f = 5!=6
print(f)
# Greater 
g = 5>6
print(g)
# less
h =6>7
print(h)
# greater than equal
i = 5>=5
print(i)
# less than equal
j = 6>=4
print(j) 

# logical operators 
# age = input("Enter your age : ") # this will return string 
age = int(input("Enter your age : "))
# print(type(age))
highschool = input("Enter highschool result : ")
decision = age >= 18 and highschool == 'Pass'
print(decision)

#
age = 5
result = None
if(age > 18 ):
    result = True 
else:
    result = False 
print("-------------------------------------")

## ternary operator 
result =  'Adult' if age > 18 else 'Minor' 
print(result)
print("--------------------------------------------")

# smallest of two no.
n1 = 32
n2 = 88
mark = n1 if n1 < n2 else n2
print(mark)  
print("-------------------------------------------------------")
