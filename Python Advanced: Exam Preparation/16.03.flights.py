def flights(*args):
    flight_data = {}

    for i in range(len(args)):

        if args[i] == "Finish":
            break

        elif not str(args[i]).isdigit():

            if args[i] not in flight_data:
                flight_data[args[i]] = 0
            flight_data[args[i]] += args[i + 1]

    return flight_data


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))