l = ['Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi','Apple','Mango','Banana','Cherry','Lichi']

# output
# index = 0 , fruit = Apple
# index = 1 , fruit = Mango
# index = 2 , fruit = Banana
# index = 3 , fruit = Cherry
# index = 4 , fruit = Lichi
# index = 5 , fruit = Apple

for index , fruit in enumerate(l):
    print(index , fruit)

print("--------------------------------------------------------------------------")

for index , fruit in enumerate(l):
    print(f'index = {index}  fruit = {fruit}')

index = 0 
for value in l:
    print(f'index = {index} , fruit = {value}')
    index = index + 1
   

    
    
