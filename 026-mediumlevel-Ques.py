# 1) check a string is palindrome or not 
def str2(original_string):
    # print(original_string)
    l = list(original_string) # convert string into list
    l.reverse()
    # print(l)
    reversed_string = ''.join(l) # join the reverse list l
    print(reversed_string)
    print(original_string)

    if original_string == reversed_string:
        return True
    else:
        return False

p = str2('pop')
print(p)

if(p):
    print('string is palindrome')
else:
    print('string is not palindrome')


# lll = ['app' , 'le' , ' man' , 'go']
# strr = ''.join(lll)
# print(strr)

# 2) Check the no. is palindrome or not
]def check(original_number):
    q1 = L1(original_number)    
    q1.reverse()    
    reversed_number = ''.join(q1)
    print("reverse_number")
    print("original_number")

    if original_number == reversed_number:
        return True
    else:
            return False

k = str(123456)
print(k)

if(k):
    print("number is palindrome") 
else:
    print("number is not palindrome")
print("---------------------------------------------------------------------------------------------")  


