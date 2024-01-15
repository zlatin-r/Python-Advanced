text = tuple(input())
symbols = {}

for char in set(text):
    symbols[char] = text.count(char)

for char, count in sorted(symbols.items()):
    print(f"{char}: {count} time/s")
