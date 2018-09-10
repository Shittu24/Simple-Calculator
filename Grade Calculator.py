x = int(input("Enter your score "))
if(x>=70):
    print("Your grade is A")
elif(x>=69 and x<=60):
    print("Your grade is B")
elif(x>=59 and x<=50):
    print("Your grade is C")
elif(x>=49 and x<=40):
    print("Your grade is D")
else:
    print("You have failed this course and need to retake it")
