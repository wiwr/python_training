'''
Created on Mar 1, 2024

@author: witek
'''
list1 = ["apple","orange",1,4,10,1,"John Hammond"]
list2 = [1,10,20,2,30]
print("List operations")
print("list1 is ", list1)
print("element at index position 4 is ", list1[4])
print("list slicing for list1[0:3]",list1[0:3])
print("Total occurences of 1 is", list1.count(1))
print("Index position of 1 is ", list1.index(1))
print("Next index position of 1 is", list1.index(1,5))
print("reverse of list is ", end="")
list1.reverse()
print("appending a value 20")
list1.append(20)
print(list1)
print("inserting a value 100 at index positon 0")
list1.insert(0,100)
print(list1)
print("sorting of list is ",end="")
list2.sort()
print(list2)
print("Removing and element")
list1.remove(4)
print("Traversing through list")
nested_list = [
    [1,2,3,4],
    list2,
    list1,
]
for value in nested_list:
    print(value)
print("Clearing a list:")
del list1[:]
print("List length is",len(list1))
print("-----------------------------------------")
list3=[]
num1 = 5
print("Provide ",num1," values")
for i in range(0, num1):
    num2=input("value:")
    list3.append(num2)
print("List that you provided contains:")
print(list3)
num1 = int(input("provide index to remove: "))
list3.pop(num1)
print(list3)

listA = [1,10,20,20,2,4,9]
print(type(listA))
listB = list(listA)
print("list1 is ",listA)
print("list2 is ",listB)
listC=listA
print(len(listA))
listA.sort()
print(listA)
listA.reverse()
print(listA)
listA.remove(20)
print(listA)
listA.insert(0,100)
print(listA)
print("listA is: ",listA)
print("listB is: ",listB)
print("listC is: ",listC)