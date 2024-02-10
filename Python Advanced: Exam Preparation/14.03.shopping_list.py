def shopping_list(budget: int, **kwargs):
    basket = 0
    result = ""

    if budget >= 100:

        for key, value in kwargs.items():
            total_price = value[0] * value[1]

            if total_price <= budget:
                budget -= total_price
                print(f"You bought {key} for {total_price:.2f} leva.")
                basket += 1

            if basket == 5:
                break
    else:
        result += "You do not have enough budget."

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
