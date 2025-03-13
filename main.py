# from index import sayHello , sum_num , email , list
# from sayuri import login , add_no , list , dict , tuple
# from func.main import difference
# from Notes.note import bbb
# print(bbb)
# q = sum_number( 5,5 )
# print(q)

# v = difference(5,9)
# print(v)


# login()
# s = add_no(4,4)
# print(s)
# print(list)
# print(dict)
# print(tuple)

# print(list)
# print(email)
# sayHello()
# v = sum_num(5,6)
# print(v)

def sum_number(*args):
    # return sum(args)
    for n in args:
        print("sum_number :", n)
sum_number(5,5)

# w = sum_number(8,1)
# print(w)
# print(sum_number())
# print(sum_number(5,10,15,20,25))