n = int(input())
odds = set()
evens = set()

for i in range(1, n + 1):
    name = input()

    ascii_sum = sum(ord(x) for x in name)
    total = ascii_sum // i

    if total % 2 != 0:
        odds.add(total)
    else:
        evens.add(total)

if sum(odds) == sum(evens):
    print(", ".join(map(str, odds.union(evens))))
elif sum(odds) > sum(evens):
    print(", ".join(map(str, odds.difference(evens))))
else:
    print(", ".join(map(str, odds.symmetric_difference(evens))))
