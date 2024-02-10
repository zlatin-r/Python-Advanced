def print_triangle(size):

    for row in range(1, size + 2):
        for num in range(1, row):
            print(num, end=" ")
        print()

    for row in range(size, 0, -1):
        for num in range(1, row):
            print(num, end=" ")
        print()
