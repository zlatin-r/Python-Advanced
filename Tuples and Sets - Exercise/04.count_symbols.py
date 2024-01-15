text = tuple(input())
symbols = {}

for char in set(text):
    symbols[char] = text.count(char)

sorted_symbols = sorted(symbols.items())
for char, count in sorted_symbols:
    print(f"{char}: {count} time/s")
