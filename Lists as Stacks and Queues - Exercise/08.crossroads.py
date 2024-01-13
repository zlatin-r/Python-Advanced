from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
passed_cars = 0
all_passed = True

command = input()
while command != "END":
    if command == "green":
        copy_green, copy_window = green_light, free_window
        while copy_green:
            if cars:
                current_car = cars.popleft()
                car_copy = current_car

                if len(car_copy) <= copy_green:
                    copy_green -= len(car_copy)
                    passed_cars += 1
                else:
                    car_copy = car_copy[copy_green:]
                    copy_green = 0

                    if len(car_copy) > copy_window:
                        car_copy = car_copy[copy_window:]
                        print(f"A crash happened!\n{current_car} was hit at {car_copy[0]}.")
                        all_passed = False
                        break
                    else:
                        passed_cars += 1
            else:
                break
    else:
        cars.append(command)
    command = input()

if all_passed:
    print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")
