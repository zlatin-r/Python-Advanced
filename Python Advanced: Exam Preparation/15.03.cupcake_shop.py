def stock_availability(flavors: list, action, *args):

    if action == "delivery":
        flavors.extend(args)
    elif action == "sell":
        if args:
            if str(args[0]).isdigit():
                flavors = flavors[args[0]:]
            else:
                for flavor in args:
                    if flavor in flavors:
                        while flavor in flavors:
                            flavors.remove(flavor)
        else:
            flavors = flavors[1:]

    return flavors


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
