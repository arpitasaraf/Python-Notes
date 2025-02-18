tuple1 = (1,2,3,4,5, 'hello' , False , None , 'hello')
print(tuple1)

# accessing 
print(tuple1[1])
print(tuple1[7])

# slicing
print(tuple1[1:8])

# length
print(len(tuple1))

# methods
# count()
print(tuple1.count('hello'))

# index()
print(tuple1.index(None))

# adding two or more tuples
t1 = (1,2,3,4)
t2 = (5,6,7,8)
t3 = t1 + t2
print(t3)
