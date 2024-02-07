def shopping_cart(*args):
    data = {"Pizza": [], "Dessert": [], "Soup": []}
    result = ""

    for arg in args:
        if arg != "Stop":
            meal, product = arg
            if meal == "Pizza" and product not in data[meal] and len(data[meal]) < 4:
                data[meal].append(product)
            elif meal == "Dessert" and product not in data[meal] and len(data[meal]) < 2:
                data[meal].append(product)
            elif meal == "Soup" and product not in data[meal] and len(data[meal]) < 3:
                data[meal].append(product)
        else:
            break

    for value in data.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_data = sorted(data.items(), key=lambda x: (-len(x[1]), x[0]))

    for items in sorted_data:
        meal_type, products = items
        result += f"{meal_type}:\n"
        for item in sorted(products):
            result += f" - {item}\n"

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))