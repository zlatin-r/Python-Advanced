from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

collection = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()

    element = curr_textile + curr_medicament

    if element == 30:
        collection["Patch"] += 1
    elif element == 40:
        collection["Bandage"] += 1
    elif element == 100:
        collection["MedKit"] += 1
    elif element > 100:
        collection["MedKit"] += 1
        medicaments[-1] += element - 100
    else:
        curr_medicament += 10
        medicaments.append(curr_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, count in sorted(collection.items(), key=lambda x: (-x[1], x[0])):
    if count > 0:
        print(f"{item} - {count}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
