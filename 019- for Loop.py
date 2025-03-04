# Iterative Through a list 
fruits = ["grape","apple","cherry","banana",]
for fruit in fruits:
    print(fruit) 

# Using 'range()' in a 'for ' loop
for i in range(11):
    print(i)

# for i in range(start,stop,step)
for j in range(1,12,1):
    print(j)

# Iterating Over Strings 
w = 'hello'
for c in w:
    print(c)

# Iterating Through Dictionaries 
# 1) Iterating Over Keys 
person = {
    "name":"kriti",
    "age":22,
    "city":"kanpur",
}
for key in person:
    print(key)

# 2) Over keys and values
for key , value in person.items():
    print(key,value) 

# 
# 2 x 1 = 2
# for i in range(2,21,2):
#     print(i)
table = 3
# for i in range(1,11):
#     print(f'{table} x {i} = {table * i}')

for i in range(1,31):
    if((table * i) % 2 == 0):
        print(f'{table} * {i} = {table * i}')  
#
person = {
    "name":"kriti",
    "age":22,
    "city":"kanpur",
}
#
print(person.items())


