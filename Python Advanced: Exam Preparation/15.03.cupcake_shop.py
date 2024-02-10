def stock_availability(flavors: list, action, *args):
    inventory_list = flavors

    if action == "delivery":
        inventory_list.extend(args)
    elif action == "sell":
        if args:

            if str(args[0]).isdigit():
                inventory_list = inventory_list[args[0]:]
            else:
                for flavor in args:

                    if flavor in inventory_list:
                        while flavor in inventory_list:
                            inventory_list.remove(flavor)
        else:
            inventory_list = inventory_list[1:]

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
