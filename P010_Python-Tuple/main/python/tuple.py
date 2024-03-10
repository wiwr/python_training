'''
Created on Mar 1, 2024

@author: witek
'''
tuple1=(1,10,20,1)
print(tuple1)
print("Total occurences of 1 is ", tuple1.count(1))
print("Length of tuple is",len(tuple1))
print("Index position of 10 is ",tuple1.index(10,0))
print("Value at index position 2 is ", tuple1[2])

tuple2=('a','b','c','d','e')
print(tuple2)

tuple3=('a',1,'someword')
print(tuple3)

tupleA=(1,10,100,40,"John",40,"john")
print(tupleA[:])
print(len(tupleA[:]))
#print(tupleA.index(1000,0))
print(tupleA.count(1000))
#tupleA[0]=5
print(tupleA)

t = ("one")
print(type(t))
for x in t:
    print(x)

t = ("one",)
print(type(t))
for x in t:
    print(x)
    
if "John" in tupleA:
    print("Is")
else:
    print("Is Not")