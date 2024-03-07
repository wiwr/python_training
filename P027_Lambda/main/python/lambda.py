'''
Created on Mar 7, 2024

@author: witek
'''
add_lambda = lambda x, y: x + y
print(add_lambda(3,5))

def sort_names_by_length(names, key_func):
    return sorted(names, key=key_func)

names = ["Alice","Bob","Charlie","David","Eve"]

sorted_names = sort_names_by_length(names, key_func=lambda x:len(x))
print("Sorted name by length:",sorted_names)

sorted_names_reverse = sort_names_by_length(names, key_func=lambda x:-len(x))
print("Sorted names by length in reverse order:", sorted_names_reverse)
names = ["Alice", "Bob", "Charlie","David","Eve","Anna","Alex"]
filtered_names = list(filter(lambda x:x.startswith("A"), map(lambda x:x.upper(), names)))
print(filtered_names)