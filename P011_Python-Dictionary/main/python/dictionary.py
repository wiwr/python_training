'''
Created on Mar 1, 2024

@author: witek
'''
dictionary1 = {
     "name":"John Wick",
     "age":40,
     "city":"London",
}
print("Dictionary operation")
print("Dictionary is",dictionary1)
print("Dictionary keys are",dictionary1.keys())
print("Dictionary values are",dictionary1.values())
print("Dictionary items are",dictionary1.items())
print("Looping though dictionary")
for key,value in dictionary1.items():
    print(key, " ", value)
print("Checking if key country exists:",dictionary1.get("country","key not found"))
print("Adding key country:")
dictionary1["country"]="UK"
print("Dictionary is ",dictionary1)
print("Removing key contry:")
dictionary1.pop("country","Key not found")
print("Dictionary is ", dictionary1)
print("---------------------------------")
dictionary2={}
key1=('name', 'age', 'city')
for name in key1:
    value=input("Provide "+name+": ")
    dictionary2[name]=value
print(dictionary2.items())
for key,value in dictionary2.items():
    print(key, " ", value)
    
dictA = {"fruit":"banana", "vegetable": "carrot"}
dictA["juice"]="mango"
dictA["beverage"]="tea"
print(dictA)
print(dictA.pop("juice","Key not found"))
print(dictA)
for key,value in dictA.items():
    print(key,value)
print()
for key in dictA:
    print(key,dictA[key])
    
D = {'jedzenie': 'Mielonka', 'ilość': 4, 'kolor': 'różowy'}
print(D['jedzenie'])
D['ilość'] +=1
print(D)

D2 = {}
D2['imię'] = 'Robert'
D2['zawód'] = 'programista'
D2['wiek'] = 40
print(D2)
print(D2['imię'])

D3 = dict(imię='Robert',zawód='programista',wiek=30)
print(D3)
D4 = dict(zip(['imię','zawód', 'wiek'], ['Robert', 'programista', 40]))
print(D4)

rec = {'dane osobowe': {'imię':'Robert', 'nazwisko':'Zielony'}, 'zawód' : ['programista', 'inżynier'], 'wiek': 40.5}
print(rec['dane osobowe'])
print(rec['dane osobowe']['nazwisko'])
print(rec['zawód'])
print(rec['zawód'][-1])
rec['zawód'].append('leśniczny')
print(rec)
rec = 0
print(rec)

D5 = {'g':1, 'b':2,'a':3}
print(D5)
D5['e'] = 99
print(D5)
print('f' in D5)
if not 'f' in D5:
    print('nie istnieje')
    print('naprawdę nie istnieje...')
    
value = D.get('x', 0)
print(value)
value = D['x'] if 'x' in D else 0
print(value)

Ks = list(D5.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
    print(key, '=>', D5[key])
    
for key in sorted(D5):
    print(key, '=>', D5[key])

for c in 'mielonka':
    print(c.upper())
    
x = 4
while x > 0:
    print('mielonka!' * x)
    x -= 1
    
squares = []
for x in [1,2,3,4,5]:
    squares.append(x ** 2)
print(squares)    
    
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)