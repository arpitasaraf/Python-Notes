# we can create list by for loop 

l = [num for num in range(1,6)]
print(l)
print("-------------------------------------")
list1 = [n**2 for n in range(1,6)]
print(list1)
print("-------------------------------------")
l2 = [n+1 for n in range(1,6)]
print(l2)
print("--------------------------------------")

# [4 x 1 = 4 , 4 x 2 = 8 , ..... ]
table = 5
m = [f'{table} * {n} = {table * n}' for n in range(1,11)]
print(m)