def shop_from_grocery_list(money, grocery, *prod_price):
    budget = money
    purchased_products = []

    for product, price in prod_price:
        if product in grocery and product not in purchased_products:
            if price <= budget:
                purchased_products.append(product)
                budget -= price
            else:
                break

    if set(grocery).issubset(purchased_products):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    rest_products = list(set(grocery).difference(purchased_products))
    rest_products.reverse()

    return f"You did not buy all the products. Missing products: {', '.join(rest_products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print("--------------------------------------------------")
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print("--------------------------------------------------")
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))