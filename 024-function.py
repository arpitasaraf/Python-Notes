def say():
    print("say")
say()
print("---------------------------------------------")

# single varaible 
def sayh(num2):
    print(num2)
sayh(25)
print("-----------------------------------------------")

# list
def sayhe(list1):
    print(list1)
sayhe([4,6,7,'sayhe'])
print("---------------------------------------------------")

# using for loop
def sayhel(list2):
    print(list2)
    for i in list2:
        print(i)
sayhel([3,6,9,12,15])
print("-----------------------------------------------------")

# return key word in function 
def sum(m1,m2):
    # print(m1,m2)
    return m1 + m2
mark = sum(7 , 6)
print(mark)
print("---------------------------------------------------------")

# circle radius or circumference 
import math
def circle(radius):
    area = math.pi * (radius)
    circumference = 2 * math.pi * radius
    return area , circumference
area , circumference = circle(6)
print(f"area:{area} , circumference : {circumference}")