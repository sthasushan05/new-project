# in sort in ascending order and descending order
list=[1,2,3,4,5,6]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
#append - helps to add the data
list1=["baka"]
list1.append(5)
print(list1)
#pop helps to delete  the given data according to the user
list2=[1,2.5,"sushan","baka","ohaiyogosaimas","sasiburi",2.5]
list2.pop(6)
print(list2)
#count helps to count the no of string in the given data
name="sushan shrestha"
number=name.count("s")
print(number)
#extend helps to combine any two data
text1=[1,2,3,4]
text2=[5,6,7,8]
text1.extend(text2)
print(text1)
#slicing
name="my name is anthony gonsalvish"
print(name[1:6])