# append()
list1 = ['A','B', 'C', 'D', 'E']
list1.append('F')
print(list1)

# pop()
list2 = ['A','B', 'C', 'D', 'E']
list2.pop()
print(list2)

# extend()
list3 = ['A','B','C','D']
list4 = ['E','F','G','H']
list3.extend(list4)
print(list3)

# insert()
list5 = ['A','B', 'C', 'D', 'E']
list5.insert(2,'world')
print(list5)

# remove()
list6 = ['A','B', 'C', 'D', 'E']
list6.remove('C')
print(list6)

# clear()
list7 = ['A','B', 'C', 'D', 'E']
list7.clear()
print(list7)

# index()
list8 = ['A','B', 'C', 'D', 'E']
index = list8.index('C')
print(index)
print(list8)

# count()
list9 =['A','B', 'C', 'D', 'E','A','D','A']
s = list9.count('A')
print(s)

# sort()
list10 = [9,4,6,2,7,1,5,8]
list10.sort()
list10.sort(reverse=True)
print(list10)

# reverse()
list11 = [9,4,6,2,7,1,5,8]
list11.reverse()
print(list11)