'''
Created on Mar 7, 2024

@author: witek
'''
if __name__ == "__main__":
    binary_data = b'Hello, World!\nThis is a test.\nPython is awesome!\n'
    buffer = bytearray(len(binary_data))
    buffer[:len(binary_data)] = binary_data
    print("Initial buffer contents:")
    print(buffer)
    with open("output.bin", "wb") as file:
        file.write(buffer)
        
    buffer.clear()
    
    with open("output.bin","rb") as file:
        file.readinto(buffer)
        content = file.read()
        print(content)