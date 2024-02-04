import os

try:
    os.remove('text.txt')
except FileNotFoundError:
    print("File already deleted!")
