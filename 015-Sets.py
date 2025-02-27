s1 = {2 , 4 , 6 , 8 }
print(s1)

# add()
s2 = {2, 4,6, 8}
s2.add(10)
print(s2)

# removing()
s3 = {2,4,6,8,10}
s3.remove(10)
print(s3)

# union()
s4 = {2,4,6,8,10}
s5 = {12,14,16,18,20}
print(s4.union(s5))

# intersection()
s6 = {2,4,6,8,10,12}
s7 = {12,14,16,18,20}
print(s6.intersection(s7))

# difference()
s9 = {2,4,6,8,10}
s10 = {12,14,16,18,20}
print(s9.difference(s10))

# symmetric_difference()
s11 = {2,4,6,8,10}
s12 = {12,14,16,18,20}
print(s11.symmetric_difference(s12))