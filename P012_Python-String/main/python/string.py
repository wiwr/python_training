'''
Created on Mar 1, 2024

@author: witek
'''
from  keyword import iskeyword
import re

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
print(S.find('ie'))
print(S.replace('ie','XYZs'))
S  = 'z' + S[1:]
print(S)
S = 'taczka'
L = list(S)
print(L)
L[0] = 'p'
print(''.join(L))
B = bytearray(b'mini')
B.extend(b'maraton')
print(B)
print(B.decode())

line = 'aaa,bbb,ccccc,ddd'
print(line.split(','))
print(S,S.upper(),S.isalpha())
line = 'aaa,bbb,ccccc,ddddd\n'
print(line)
print(line.rstrip())
print(line.rstrip().split(','))

print('%s, jajka i %s' % ('mielonka', 'MIELONKA!'))
print('{0}, jajka i {1}'.format('mielonka','MIELONKA!'))
print('{}, jajka i {}'.format('mielonka','MIELONKA!'))

print('{:,.2f}'.format(2969999.2567))
print('%.2f | %+05d' % (3.14159, 42))
print(dir(S))
print(help(S.replace))
msg = """ aaaaaaaaaaaaaaaaaaaaaaaa
bbbb'''bbbbbbbbbb""bbbbbbbb'bbbb
cccccccccccccccccccccccccccccc
"""
print(msg)
print(r'C:\tekst\nowy')
print('sp\xc4m')
print(b'a\x01c')
print(u'sp\u00c4m')
print('spam')
print('spam'.encode('utf8'))
print('spam'.encode('utf16'))

match = re.match("Witaj,[\t]*(.*)Robinie", 'Witaj, sir    Robinie')
print(match.group(1))
match = re.match('[/:](.*)[/:](.*)[/:](.*)','/usr/home:lumberjack')
match.groups()
print(re.split('[/:]','/usr/home/luberjack'))

name = "Mielonka"
x = F'Hello {name} {["test", "test1"]}'
print(x)

text = "Hi Mielonka, Witaj, Sir Robin"
x = {char: text.count(char) for char in set(text)}
print(x)
#sort
#exclude special characters
#all lowercase