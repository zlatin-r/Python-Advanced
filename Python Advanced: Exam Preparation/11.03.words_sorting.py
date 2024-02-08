def words_sorting(*args):
    data = {}
    result = ""

    for word in args:
        ascii_sum = 0
        for i in range(len(word)):
            ascii_sum += ord(word[i])
        data[word] = ascii_sum

    if sum(data.values()) % 2 != 0:
        sorted_data = sorted(data.items(), key=lambda x: -x[1])
    else:
        sorted_data = sorted(data.items())

    for key, value in sorted_data:
        result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
