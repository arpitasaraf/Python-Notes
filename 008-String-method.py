# strip()
username = '     mohd hamza     '
newUsername = username.strip()
print(newUsername)
print(username)

# Lower()
email = 'Hamza@gmail.COM'
newEmail = email.lower()
print(newEmail)

# upper()
gender = 'male'
newGender = gender.upper()
print(newGender)

# replace()
rep = "My name is Hamza"
newRep = rep.replace('Hamza','Mohd Hamza')
print(newRep)

# startwith()
s = "C programming"
print(s.startswith("C"))

# endwith()
s = "document.txt"
print(s.endswith(".txt"))

# find(substring)
s = "Hello, World"
print(s.find("World"))
print(s.find("program"))

# count()
a = "banana"
print(a.count("n"))

# capitalize()
s = "programming jhk"
print(s.capitalize())

# title()
s = "hello world"
print(s.title())

# isalpha()
s = "DAA" 
print(s.isalpha())
w = "daa234"
print(w.isalpha())

# isdigit()
s = "12345"
print(s.isdigit())
w = "12345daa"
print(w.isdigit())

# islower()
s = "hello"
print(s.islower())
w = "World"
print(w.islower())

# isupper()
s ="WORLD"
print(s.isupper())
w = "hello"
print(w.isupper())

# Format()
s = "My name is {} and I am {} years old."
print(s.format("jayanti",22))

# Formate string()
name = 'hamza'
gender = 'male'

info = f'My name is {name}. And I am {gender}'
print(info)
