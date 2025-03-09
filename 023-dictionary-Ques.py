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

