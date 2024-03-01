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