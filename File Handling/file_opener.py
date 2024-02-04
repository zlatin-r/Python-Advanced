try:
    file = open("resources/text.txt", "r")
    print("File found")
except FileNotFoundError:
    print("File not found")
