'''
Created on Mar 7, 2024

@author: witek
'''
import os
import json

if __name__ == "__main__":
    file_path = "example.json"
    file_path2 = "example2.json"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        print(data)
        data["Country"]="UK"
        
        if "city" in data:
            del data["city"]
            
        with open(file_path2, "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        with open(file_path2, "r") as json_file:
            data = json.load(json_file)
        print(data)
    else:
        print("File doesn't exist.")