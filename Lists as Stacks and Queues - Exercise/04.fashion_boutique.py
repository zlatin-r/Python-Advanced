clothes_in_box = list(int(x) for x in input().split())
rack_capacity = int(input())
rack_counter = 1
sum_values = 0

while clothes_in_box:
    current_value = clothes_in_box.pop()
    if current_value + sum_values == rack_capacity:
        if clothes_in_box:
            rack_counter += 1
            sum_values = 0
    elif current_value + sum_values > rack_capacity:
        rack_counter += 1
        sum_values = 0
        sum_values += current_value
    else:
        sum_values += current_value

print(rack_counter)
