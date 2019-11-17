'''import sys
name=input("enter your name")
for x in range(1,9):
   if name.isalpha() == True or ' ' in name:
        if len(name) >= 3 :
            pass
            break

        else:
            print("invalid")
            name=input("enter your name")
   else:
       print("invalid")
       name = input("enter your name")
age=input("enter your age")
while int(age) < 18:
    print("enter the age above 18")
    age=input("enter your age")
phn_no=input("enter your number")
while len(phn_no)!=10:
    print("enter the correct number")
    phn_no=input("enter your number")'''
#write a program to print the multiplication table of the number entered by the user
'''num=int(input("enter the number"))
print("the multiplication table is %s" % num)
for x in range(1,11):
    print("%s * %s = %s" %(num, x, num*x))'''
#from a list of number make a new list cotaining only the even number
'''list=[]
i=0
n=int(input("enter the number of elements"))
while i<n:
    print("enter the element")
    element=int(input())
    list.append(element)
    i+=1
print(list)
even_list=[]
for i in list:
    if i%2==0:
        even_list.append(i)
print("the even number list is:", even_list)'''
#ask the user to enter 10 number using only one input statement
'''input_list=input("enter the number with commas")
list=input_list.split()
print("the list is ",list)
'''
import calendar