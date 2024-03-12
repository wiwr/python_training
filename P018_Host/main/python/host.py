'''
Created on Mar 5, 2024

@author: witek
'''
import platform as p

if __name__ == "__main__":
    print("Platform:",p.platform())
    print("Machine type:",p.machine())
    print("Processor type:",p.processor())
    print("Operating system:",p.system())
    print("Operating system version:",p.version())
    print("Python implementation",p.python_implementation())
    print("Python version typle:", p.python_version_tuple())
    print("Python version:",p.python_version())
