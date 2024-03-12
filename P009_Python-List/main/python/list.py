'''
Created on Mar 1, 2024

@author: witek
'''
list1 = ["apple", "orange", 1, 4, 10, 1, "John Hammond"]
list2 = [1, 10, 20, 2, 30]
print("List operations")
print("list1 is ", list1)
print("element at index position 4 is ", list1[4])
print("list slicing for list1[0:3]", list1[0:3])
print("Total occurences of 1 is", list1.count(1))
print("Index position of 1 is ", list1.index(1))
print("Next index position of 1 is", list1.index(1, 5))
print("reverse of list is ", end="")
list1.reverse()
print("appending a value 20")
list1.append(20)
print(list1)
print("inserting a value 100 at index positon 0")
list1.insert(0, 100)
print(list1)
print("sorting of list is ", end="")
list2.sort()
print(list2)
print("Removing and element")
list1.remove(4)
print("Traversing through list")
nested_list = [
    [1, 2, 3, 4],
    list2,
    list1,
]
for value in nested_list:
    print(value)
print("Clearing a list:")
del list1[:]
print("List length is", len(list1))
print("-----------------------------------------")
list3 = []
num1 = 5
print("Provide ", num1, " values")
# for i in range(0, num1):
#     num2=input("value:")
#     list3.append(num2)
# print("List that you provided contains:")
# print(list3)
# num1 = int(input("provide index to remove: "))
# list3.pop(num1)
# print(list3)

listA = [1, 10, 20, 20, 2, 4, 9]
a, b, c, d, e, f, g = listA
print(a, b, c, d, e, f, g)
print(type(listA))
listB = list(listA)
print("list1 is ", listA)
print("list2 is ", listB)
listC = listA
print(len(listA))
listA.sort()
print(listA)
listA.reverse()
print(listA)
listA.remove(20)
print(listA)
listA.insert(0, 100)
print(listA)
print("listA is: ", listA)
print("listB is: ", listB)
print("listC is: ", listC)

L = [123, "mielonka", 1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L + [4, 5, 6])
print(L * 2)
print(L)
L.append('NI')
print(L)
L.pop(2)
print(L)
M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M)
print(M[1])
print(M[1][2])
col2 = [row[1] for row in M]
print(col2)
print([row[1] + 1 for row in M])
print([row[1] for row in M if row[1] % 2 == 0])
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c * 2 for c in 'mielonka']
print(doubles)
print(list(range(24)))
print(list(range(-16, 17, 2)))
print([[x ** 2, x ** 3] for x in range(7)])
print([[x, x / 2, x * 2] for x in range(-16, 17, 2) if x > 0])
G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))
print(list(map(sum, M)))
print({sum(row) for row in M})
print({i: sum(M[i]) for i in range(3)})
print([ord(x) for x in 'mielonka'])
print({ord(x) for x in 'mielonka'})
print({x: ord(x) for x in 'mielonka'})
print((ord(x) for x in 'mielonka'))

listC = [[1, 2], [3, 4], [5, 6], [-1, 4], [-2, 5], [-3, 7]]
print(listC)
listC.sort(key=lambda x: x[0] + x[1])
print(listC)
listC.sort(key=lambda x: x[1])
print(listC)

listD = [[0] * 5, [1] * 7, [2] * 3]
print(listD)
listE = [1 , 2, 3, 4, 5]
listF = listD[0] + listD[1] + listD[2] + listE
print(listF)
listF.sort()
print(listF)
listG = listF[::2]
print(listG)
listH = listG[::-1]
print(listH)
listI = [x * x for x in listH]
print(listI)

uniques = []
for num in listF:
    if num not in uniques:
        uniques.append(num)
print(uniques)

listJ = ["one", "two", "three", "four", "five"]
print(len(listJ))
print(listJ)

