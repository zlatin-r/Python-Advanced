import os

try:
    os.remove('resources/text.txt')
except FileNotFoundError:
    print("File already deleted!")
