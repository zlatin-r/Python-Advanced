def concatenate(*args, **kwargs):
    result = ''

    for arg in args:
        if arg in kwargs.keys():
            result += kwargs[arg]
        else:
            result += arg

    for key in kwargs.keys():
        if key in result:
            result = result.replace(key, kwargs[key])

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
