'''take five marks input from the user and then input it into the list and then print the sum of all the marks'''
math=int(input("enter you math marks"))
science=int(input("enter your science marks"))
social=int(input("enter your fucking social marks"))
nepali=int(input("mask hal nepali ko"))
computer=int(input("computer ka marks dalo"))
list=[math,science,social,nepali,computer]
print(list)
total=sum(list)
print("the total marks obtained in all subject =",total)
