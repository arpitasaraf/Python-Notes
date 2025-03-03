# 1) basic conditionals
age = 18 
if age > 18:
    print("you can drive")
else:
    print(" you can not drive")

# 2) multiple conditionals
score = 85
if score >= 80:
    print("Grade:A")
elif score >= 90:
    print("Grade:B")
elif score >= 70:
    print("grade:C")
else:
    print("Grade:F")

# 3) using logical operators
temperature = 25
if temperature > 30:
    print("it's hot outside.")
elif temperature <15:
    print("it's cold outside.")
else:
    print("the whether is moderatte.")

# 4) Nested conditionals
n1 = 7
if n1 > 0:
    if n1 % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("number is not positive")


## 1) WAP to check if a number is positive , negative or zero?
n2 = int(input("enter a number:"))
if n2 >= 1:
    print("positive")
elif n2 < 0:
    print("negative")
else:
    print("zero ") 

## 2) WAP to campare two numbers and print the large number?
n3 = int(input("enter 1st numbers :"))
n4 = int(input("enter 2nd numbers:"))
if n3 > n4:
    print(n3)
else:
    print(n4)

## 3) WAP to check if two string are equal.
n5 = "hello"
n6 = "world"
if n5 == n6:
    print(n5)
else:
    print(n6)

## 4) WAP to find the smallest of two numbers.
n7 = int(input("enter 1st no:"))
n8 = int(input("enter 2nd no:"))
if n7 < n8:
    print(n7)
elif n7 == n8:
    print("both no are equals :")
else:
    print(n8)

# ## 5) WAP to check if a given no. is divisible by both 3 and 5?
n10 = int(input("enter no. :")) 
if n10 % 3 == 0:
    if n10 % 5 == 0:
        print("no. is divisible by 3 and 5.")
    else:      
        print("no. is divisible by 3 and NOT 5.")
elif n10 % 5 == 0:
    print("no. is NOT divisible by 3 and is divisible by 5.")
else:
    print("no. is NOT divisible by 3 and 5. ")

## 6) WAP to check if a no. lies between 10 and 50 (inclusive). 
n = int(input("enter any no.:"))
if n >= 10 and n <= 50:
    print('no. is between')
else:
    print('no. is not between')


## 7) WAP to find if a no. is odd or even ?
n = int(input("enter any no:"))
if n % 2 == 0:
    print("even no.")
else:
    print("odd no. ") 

## 8) WAP to create program that prints "welcome" if the user's age greater than 18?
age = int(input("enter your age:"))

if age>=18:
    print("you can access apply for job ")
else:
    print(" you cannot access to apply for job")

## 9) WAP to check if a person is eligible to vote based on their age(age>=18).
n = int(input("enter your age:"))
if n >=18:
    print(" you can apply for vote.")
else:
    print("you cannot apply for vote. ") 

## 10) to check if a number is divisible by 4. 
    # if true, print "Divisible", otherwise print "Not divisible".NotADirectoryError 
n = int(input("enter any no:"))
if n % 2 == 0:
    print("divisible no.")
else:
    print("not divisile no. ") 

## 11) WAP to determine if a character is a vowel or a consonant?
s= input("enter any character :")

if (s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s=='I' or s == 'O' or s == 'U'):
    print(s , 'is a vowel')
else:
    print(s,'is a consonant')

## 12) Create a program that checks if a number is positive. If true, print "Positive"; otherwise, print "Negative or Zero".
n = int(input("enter a no. :"))
if n >0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("equal to zero ")


## 13) Check if a given year is a leap year or not. write the program
year = int(input("enter a year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year ")
    
