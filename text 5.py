#write a program to tell if the user is eligible to drive or not
'''mark=int(input("enter your marks"))
if(int(mark>=40)):
    print("pass")
else:
    print ("sorry")'''
#write the program eligible to drive
'''age=int(input("enter your age"))
if(int(age>=18)):
    print("congratulation you are eligible to drive")
else:
    print("sorry you are not eligible")'''
#write a program for grading the student based in the marks
'''90 to 100-a-A
70-90-B
40-70-C
below 40-fail'''
mark=int(input("enter your marks"))
if(int(mark>=90 and mark<100)):
    print("div=A")
elif(int(mark>=70 and mark<90)):
    print("div=B")
elif(int(mark>=40 and mark<70)):
    print("div=C")
elif(int(mark<40 and mark>=0)):
    print("fail")
else:
    print("invalid")
#odd or even
'''number=int(input("enter the number"))
if(int(number%2==0)):
    print("even")
else:
    print("odd")'''
'''year=int(input("enter the year"))
if (year%400==0):
     print("leap year")
elif (year%4==0 and year%100!=0):
    print("leap year")
else:
     print("not leap year")'''

'''import sys
name=str(input("enter your name"))
if name.isalpha()==True:
    if len(name)>=3:
        pass
    else:
        sys.exit("invalid input ")
else:
    print("invalid")
age=(input("enter your age"))
if age.isnumeric()==True:
    if age>=18 and age<120:
        pass
else:
    sys.exit("invalid input ")
mobno=int(input("enter your no"))
if len(str(mobno))==10:
    pass
else:
    sys.exit("invalid input ")
'''
