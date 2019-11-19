#to write until user want
'''f=open("file.txt",'w')
text=input("write what ever you like")
while text!='quit':
    f.writelines(text+'\n')
    text=input("chup")
print("done")
f.close()

#to open the save file
with open("file.txt",'r') as f:
    text=f.read()
print(text)

#append
f=open('file.txt','a')
text1=input("write your name")
while text1!='quit':
        f.writelines(text1+"\n")
        text1=input("bhat khais")
print("done")
f.close()'''

'''#sajilo read and write
f=open("text2.txt",'w+')
f.writelines("hello earth")
f.seek(6)
f.writelines("world")
f.close()'''

#map function
'''def cube(c):
    return c**3
lst=[2,3,1,4,5]
lst4=list(map(cube,lst))
print(lst4)'''

#lambda=works directly with out defining function
'''lst=[1,2,3,4]
lst_n1=list(map(lambda x:x**2,lst))
print(lst_n1)'''

#filter
def filter1(a):
    if a%2==0:
        return True
    else :
        return False
num=[1,1,2,3,3,2,3,5,1,3,562,3,6,2,3,2,6,2,6,2,3,5]
lst=list(filter(filter1,num))
print(lst)
#write a program that copies content of one file to other file

#write a program that correct this
#write a program to find prime number form 1 to 2500 usinglist comprehension
#write a program that usrs map to convert a list temp a fahrenheit to celcius