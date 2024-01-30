numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line

    try:                                                  # try block to test for ValueError added
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:                                    # except block added to handles the error if occurs
        print("The variable number must be an integer")

    line = input()                                        # second input in to the while loop added

line = input()

while line != "Remove":
    searched = line

    print(numbers_dictionary[searched])

    line = input()                                        # second input in to the while loop added

line = input()

while line != "End":
    searched = line

    try:                                                  # try block to test for KeyError added
        del numbers_dictionary[searched]
    except KeyError:                                      # except block added to handle the error if occurs
        print("Number does not exist in dictionary")

    line = input()                                        # second input in to the while loop added

print(numbers_dictionary)
