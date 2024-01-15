n = int(input())
table = set()

for _ in range(n):
    element = input().split()
    for i in element:
        table.add(i)

for el in table:
    print(el)
