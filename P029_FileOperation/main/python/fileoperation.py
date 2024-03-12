'''
Created on Mar 7, 2024

@author: witek
'''
import errno
import os

if __name__ == "__main__":
    print(os.getcwd())
    try:
        with open("Example.txt","r") as file:
            content = file.read()
            print(content)
            
    except IOError as e:
        if e.errno == errno.ENOENT:
            print("File not found!")
        else:
            print("An error occurred:",e)
            
    file_path = "example.txt"
    file = open(file_path, "a")
    
    file.write("\nHello, World!\n")
    file.write("This is a test.\n")
    file.write("Python is awesome!\n")
    
    file.close()
    
    file = open(file_path, "r")
    
    content = file.read()
    print("Content of the file (using read()):")
    print(content)
    
    file.close()
    
    file = open(file_path, "r")
    
    print("\nContent of the file (using readline()):")
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
        
    file.close()
    
    file = open(file_path, "r")
    print("\nContent of the file (using readlines()):")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        
    file.close()