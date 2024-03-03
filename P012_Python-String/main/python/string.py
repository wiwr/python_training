'''
Created on Mar 1, 2024

@author: witek
'''
from  keyword import iskeyword

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

string1=('the quick brown'
        'fox jumped over'
        'the lazy dog'
        )
print(string1)
print(iskeyword('print'))
print(iskeyword('if'))
print(iskeyword('for'))
print("----------------------")
S = 'Mielonka'
print("S = ",S)
print("Length of S: ", len(S))
print("First character in S: ", S[0])
print("Second character in S: ", S[1])
print("Last character in S:" , S[-1])
print("Before last character in S:", S[-2])
print("Part of string: ",S[1:3])
print("S[1:] -", S[1:])
print("S[0:7]",S[0:7])
print("S[:7]",S[:7])
print("S[:-1]",S[:-1])
print("S[:]",S[:])
print(S + 'xyz')
print(S * 8)