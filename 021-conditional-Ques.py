# 
score = int(input("enter a marks score:"))
if (score < 0 or score > 100):
    print('score is invalid')
elif (score >= 91 and score <=100):
    print("A+")
elif (score>=81 and score<=90):
    print("A")
elif (score>=71 and score<=80):
    print("B+")
elif(score>=61 and score<=70):
    print("B")
elif(score>=51 and score<=60):
    print("C+")
elif(score>=41 and score<=50):
    print("C")
else:
    print("F")
