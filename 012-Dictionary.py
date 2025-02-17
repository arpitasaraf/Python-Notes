# Dictionary
my_dic = {
    "name":"Kriti",
    'email':'kriti@gmail.com',
    "phone":8524647,
    'isfemale':True,
}
print(my_dic)

# Accessing
print(my_dic['email'])
print(my_dic['isfemale'])
print(my_dic['name'])
print(my_dic['phone'])

# update
my_dic['name'] = 'Karishma'
print(my_dic)

# delete
del my_dic['email']
print(my_dic)

# adding 
my_dic['address'] = 'C-383 Allahabad'
print(my_dic)

my_dic['pincode'] = 202312
print(my_dic)