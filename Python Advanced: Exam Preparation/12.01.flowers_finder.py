from collections import deque

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

vowels = deque(input().split())
consonants = input().split()

word_found = False

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()

    for flower in flowers.keys():
        flowers[flower] = flowers[flower].replace(v, "")
        flowers[flower] = flowers[flower].replace(c, "")

        if flowers[flower] == "":
            print(f"Word found: {flower}")
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
