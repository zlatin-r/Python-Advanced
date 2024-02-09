def naughty_or_nice_list(kids: list, *args, **kwargs):
    data = {}
    naughty_kids = []
    nice_kids = []
    not_found_kids = []

    if args:
        for arg in args:
            num, behavior = arg.split('-')
            record = tuple(f"{int(num)}-{behavior}")

            if kids.count(record) == 1:
                pass


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))