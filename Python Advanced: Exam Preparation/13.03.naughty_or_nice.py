def naughty_or_nice_list(kids: list, *args, **kwargs):
    data = {"Nice": [], "Naughty": [], "Not found": []}
    result = ""

    def num_count(kids_data: list, number):
        counter = 0
        for record in kids_data:
            digit = record[0]
            if digit == number:
                counter += 1
        if counter == 1:
            return True

    def name_count_check(kids_data, name):
        counter = 0
        for record in kids_data:
            if record[1] == name:
                counter += 1
        if counter == 1:
            return True

    def remove_kid_args(kids_data, number):
        for record in kids_data:
            digit = record[0]
            if digit == number:
                kids_data.remove(record)
                return record[1]

    def remove_kid_kwargs(kids_data, number):
        for record in kids_data:
            digit = record[1]
            if digit == number:
                kids_data.remove(record)
                return record[1]

    for info in args:
        number, behavior = info.split("-")
        if num_count(kids, int(number)):
            if behavior == "Nice":
                data["Nice"].append(remove_kid_args(kids, int(number)))
            elif behavior == "Naughty":
                data["Naughty"].append(remove_kid_args(kids, int(number)))

    if kwargs:
        for name, behavior in kwargs.items():
            if name_count_check(kids, name):
                if behavior == "Nice":
                    data["Nice"].append(remove_kid_kwargs(kids, name))
                elif behavior == "Naughty":
                    data["Naughty"].append(remove_kid_kwargs(kids, name))

    if kids:
        for record in kids:
            data["Not found"].append(record[1])

    if data["Nice"]:
        result += f"Nice: {', '.join(data['Nice'])}\n"
    if data["Naughty"]:
        result += f"Naughty: {', '.join(data['Naughty'])}\n"
    if data["Not found"]:
        result += f"Not found: {', '.join(data['Not found'])}"

    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))