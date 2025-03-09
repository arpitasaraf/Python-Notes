# 1) find the vowels from the user given string.
def s1(str):
    vowels = "aeiouAEIOU"
    count = 0
    # fff = 'a' in vowels
    # print(fff)
    for c in str:
        print(c)
        if ( c in vowels):
            count = count + 1
    return count 
count = s1("saruri1")
print("no. of vowels :" , count)
print("---------------------------------------------------")

# 2) parameters is not given it will given by default parameters.
def s2(str='karishma'):
    vowels = "aeiouAEIOU"
    count = 0
    for c in str:
        if (c in vowels):
            count = count + 1
    return count
count = s2()
print("no. of vowels :",count)
print("------------------------------------------------------------------------")

# 3) with both parameters
def s3(str = "jayanti"):
    vowels = "aeiouAEIUO"
    count = 0
    for c in str:
        if ( c in vowels ):
            count = count + 1
    return count
count = s3( ' kriti , payal ' )
print("no. of vowels : " , count)
print(""""""""""""""""""""""""""""""""""""""""""""")
