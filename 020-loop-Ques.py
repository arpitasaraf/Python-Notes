# 1) 
# for i in range(1,11):
#     print(i)

# 2)
l = [2,4,6,8 ,10]
for i in l:
    print(i)

# 3)
for i in range(1,21):
    if (i%2==0):
        print("even",i)
        
## 1) WAP to print the  numbers from 1 to 10 using a for loop
for i in range(1,11):
    print(i)


## 2) WAP to  print the elements of an array one by one using a for loop,
#     in this question array(means) as a list. 
l = [2,4,6,8 ,10]
for i in l:
    print(i)


## 3) WAP to print all even numbers between 1 and 20 using a for loop
for i in range(1,21):
    if (i%2==0):
        print("even",i)


## 4) WAP for loop to calculate the sum of all numbers from 1 to 100.
total = 0
for num in range(1,101):
    total += num
    print(total)
    # print("sum of two no. : ",total)


## 5) WAP to  Print a multiplication table for the number 5 using a for loop.
num = 5
for  i in range(1,11):
    print(f"{num} x {i} = {num * i}")

  
## 6) Write a for loop to print a triangle of stars (*), like this:
    # *
    # **
    # ***
    # ****
    # *****
rows = int(input("enter a rows : "))
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print(" ")


##  7) write a python program to Print the reverse of an array using a for loop.
my_lists = [1, 2, 3, 4, 5]
for num in reversed(my_lists):
  print(num)
print(num)


## 8) WAP to Use a loop to print all numbers divisible by 3 between 1 and 30.
for num in range(1,31):
    if num % 3 == 0:
        print(num)

