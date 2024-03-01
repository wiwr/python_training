'''
Created on Mar 1, 2024

@author: witek
'''
full_name = "John Hammond doesn\'t wait\nJurassic Park\nJurassic World"
print("String Operations")
print("String is ", full_name)
print("Character at index position 2 is ", full_name[2])
print("Slicing string full_name[0:5]",full_name[0:5])
print("Second line of string is ",full_name.splitlines()[1])
print("Unicode value for A is ",ord('A'))
print("Character value for unicode value 65 is ", chr(65))
print("Looping through string")
for character in full_name:
    print(character,end="")

first_name = "John"
last_name = "Hammondmm"
print("Adding whilespace using join function")
print(" ".join(first_name))
print("Splitting string")
print(full_name.split("\n"))
print("Sorting string",first_name)
print(sorted(first_name))
print("Finding index of substring mm in",end=":")
print(last_name.find("mm"))
print("Finding index of substring mm in",end=":")
print(last_name.index("mm"))
print("Finding index of substring mm in",end=":")
print(last_name.rfind("mm"))
print("String concatenation",first_name + last_name)
print("String multiplication",3* "py")