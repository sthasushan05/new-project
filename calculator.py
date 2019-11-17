import calendar
import sys
name=input("enter your name\n")
for x in range(1,9):
    if name.isalpha()==True or ' ' in name:
        if len(name)>=3:
            pass
            break
        else:
            print("error")
            name=input("enter your name\n")
    else:
        print("error")
        name=input("enter your name\n")
age=input("enter your age\n")
while int(age)<15:
    print("enter the age ")
    age=input("enter your age\n")
mob_no=input("enter your number\n")
while len(mob_no)!=10:
    print("the correct number")
    mob_no=input("enter your number\n")

#calculator


print("choose the number of the operataon you want\n1.addition\n2.subtraction\n3.division\n4.multiplication\n5.square\n6.cube\n7.square root\n8.calander")
select=int(input("select the number: \n"))

if(int(select==1)):
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} + {} = '.format(number_1, number_2),number_1 + number_2)
elif(int(select==2)):
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} - {} = '.format(number_1, number_2),number_1 - number_2)
elif(int(select == 3)):
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} / {} = '.format(number_1, number_2), number_1 / number_2)
elif(int(select==4)):
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    print('{} * {} = '.format(number_1, number_2),number_1 * number_2)
elif(int(select==5)):
    number_1 = int(input('Enter your number: '))
    print('{}² = '.format(number_1),number_1 * number_1)
elif (int(select == 6)):
    number_1 = int(input('Enter your number: '))
    print('{}³ = '.format(number_1), number_1 * number_1 *number_1)
elif (int(select == 7)):
    number_1 = int(input('Enter your first number: '))
    print('{}½ = '.format(number_1), number_1 /0.5)
elif(int(select==8)):
    yy=int(input("enter the year"))
    mm=int(input("enter the month"))
    print(calendar.month(yy , mm))
else:
    print("the number you dial is incorrect please try again")
    sys.exit()