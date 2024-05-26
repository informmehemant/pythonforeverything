import os
print(os.getcwd())
try:
    with open('./files/myFile.txt') as f:
        lines = [line.strip() for line in f]
        print(lines)
except FileNotFoundError:
    print("File 'myFile.txt' not found!")
except PermissionError:
    print("Error: You don't have read permission for 'myFile.txt'")