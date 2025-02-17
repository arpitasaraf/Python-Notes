# string slicing()
str1 = 'Mohd Hamza'
s1 = str1[0:4]
s2 = str1[5:10]
print(s1)
print(s2)

# start from an index and go to end 

email = 'mohdhamza@gmail.com'
s3 = email[4:]
print(s3)

#  start from beginning and go to an index 
address = 'H-D Shams Nagar'
s5 = address[:9]
print(s5)

# string with gap use 
str = "0123456789"
s7 = str[0::2]
print(s7)

# string with use len(str) for skipping 1 digit no. 
str = "0123456789"
s7 = str[0:len(str):2]
print(s7)

# count and calculated the string length()
length_of_str = len(str)
print(length_of_str)