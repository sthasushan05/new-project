import calendar
import sys
'''name=input("enter your name\n")
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
    if mob_no.isdecimal()==True:
        print("the correct number")
        mob_no=input("enter your number\n")
    else:
        print("invalid")
        mob_no=input("enter the number")'''
#calculator

def calculator():
    return('{} + {} = '.format(number_1, number_2), number_1 + number_2)

print("choose the number of the operataon you want\n1.addition\n2.subtraction\n3.division\n4.multiplication\n5.square\n6.cube\n7.square root\n8.cube root\n9.calander")
select=int(input("select the number: \n"))
select = 0
while select ==0:
    if(int(select==1)):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

    elif(int(select==2)):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        print('{} - {} = '.format(number_1, number_2),number_1 - number_2)
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif(int(select == 3)):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        print('{} / {} = '.format(number_1, number_2), number_1 / number_2)
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif(int(select==4)):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        print('{} * {} = '.format(number_1, number_2),number_1 * number_2)
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif(int(select==5)):
        number_1 = int(input('Enter your number: '))
        print('{}² = '.format(number_1),number_1 * number_1)
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif (int(select == 6)):
        number_1 = int(input('Enter your number: '))
        print('{}³ = '.format(number_1), number_1 * number_1 *number_1)
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif (int(select == 7)):
        number_1 = int(input('Enter your first number: '))
        print('{}½ = '.format(number_1), number_1 **0.5)
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif(int(select==8)):
        number_1=int(input("enter the number you want to cube"))
        print('{}**()1/3 = '.format(number_1),number_1**(1/3))
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    elif(int(select==9)):
        yy=int(input("enter the year"))
        mm=int(input("enter the month"))
        print(calendar.month(yy , mm))
        choice = input("1.menu\n2.exit")
        if choice == 1:
            calculator()
        else:
            sys.exit("thanks for using")
    else:
        print("the number you dial is incorrect please try again")
        sys.exit()
calculator()
