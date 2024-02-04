import re

words_count = {}

with open("resources/words.txt") as file:
    searched_words_as_text = file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]

with open("resources/input.txt") as file:
    content = file.read().lower()


for word in searched_words:
    pattern = re.compile(rf"\b{word}\b")
    result = re.findall(pattern, content)

    words_count[word] = len(result)

sorted_words_count = sorted(words_count.items(), key=lambda x: -x[1])

with open("resources/output.txt", "a") as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")
