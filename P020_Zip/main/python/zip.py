'''
Created on Mar 5, 2024

@author: witek
'''
names = ['Jan', 'Karol','Paweł','Adam']
ages = [50,49,37,21]
eye_colors = ['niebieski', 'brązowy', 'brązowy','green']

print(list(zip(names,ages,eye_colors)))

for name, age, eye_color in zip(names, ages, eye_colors):
    if age > 40:
        print(name)
    print(eye_color)