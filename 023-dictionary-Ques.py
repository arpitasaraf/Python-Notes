# 1) WAP to create an object account with properties username , password and isLoggedIn . write an if-else statement to check: 
     # If isLoggedIn is true , print" Welcome,". Otherwise , print "Please log in."
dict = {
    "username":"karishma",
    "password":"drthjika",
    "isloggedIn":False
}
# print(dict)
if (dict["isloggedIn"]):
        print("welcome")
else:
        print("Please Log in.")
print("-------------------------------------------------------------------------------------------------------------------------

# 2) WAP to create an object product with properties name, catergory, and in Stock. 
    # Use an if-else condition to check if instock is false.
    # if yes , print is Out of Stock:,otherwise print :avaiable",
dict = {
    "name": "manvi",
    "category":"electronics",
    "inStock":False
}
if not product["inStock"]:
    print(f'{product["name"]} is Out of stock')
else:
    print(f'{product["name"]} is available')
print("------------------------------------------------------")

# 3) WAP to create an object user with properties age , isverified and isAdmin. Use an if-else condition.
    # if isAdmin is ture,print "admin Access Granted".
    # Else if isverifed is true , print"user access granted".
    # otherwise,print"access denied".
dict = {
    "age":30,
    "isverified":True,
    "isAdmin":True
}
if user["isAdmin"]:
    print("admin access Granted")
elif user["isverified"]:
    print("user access granted")
else:
    print("access denied")
print("------------------------------------------------------------------------------------------------")

# 4) WAP to given an object student with properties name , age and address do the following :
     # i) if the age is 18 less than 18 ,update the address to "not provided".
     # ii) if the age is 18 or greater, detel the address property.
child = {
    "name":"anchal",
    "age": 30,
    "address":"UP80 Agra "
}
if child["age"]:
    child["address"] = "not provided"
else:
    del child["address"]
print(child)
print("--------------------------------------------------------------------------------------------------------") 

# 5) WAP to given an object product with properties name , category , price and discount do the following:
     # i) if the price is greater than 100 , update the discount to "15%".
     # ii) if the price is less than or equal to 100 , delet the discount property.

# 6) WAP to given an object userProfile with properties name , email, and phonenumbers,performance the following:
     # i) if the email exists , update the phonenumber to "not Provide".
     # ii) if the email does not exist , delete the name property.
