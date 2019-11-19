#area of circle
'''def radius(r):
    area=22/7*r*r
    return area
r=input("enter the radius of circle")
area=radius(float(r))
print("son of  a bitch",area)'''


#pow of number
'''def pow(a,b):
    power=a**b
    return power
a=input("enter the vlaue")
b=input("enter the power")
power=pow(float(a),float(b))
print("fuck off",power)'''


#armstrong number
def a_strong(a):
    power=len(str(a))
    sum=0
    while a>0:
        num=a%10
        sum=sum+num**power
        a//=10
    return sum



strong=int(input("enter the armstrongg number"))
goat=a_strong(strong)
if goat==strong:
    print("hello world")
else:
    print("fuck off")


#palindrome
def pal(p):
    rev=0
    while p>0:
        num=p%10
        rev=rev*10+num
        p=p//10
    return rev



pal_num=int(input("enter the number"))
ohaiyo=pal(pal_num)
if ohaiyo==pal_num:
    print("ohiyogosaimas")
else:
    print("baka")