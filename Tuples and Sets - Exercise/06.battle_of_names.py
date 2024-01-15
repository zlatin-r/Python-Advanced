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
    union = odds.union(evens)
    print(", ".join(map(str, union)))
elif sum(odds) > sum(evens):
    difference = odds - evens
    print(", ".join(map(str, difference)))
else:
    sym_difference = odds.symmetric_difference(evens)
    print(", ".join(map(str, sym_difference)))
