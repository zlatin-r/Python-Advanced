odds = set()
evens = set()

for i in range(1, int(input()) + 1):

    ascii_sum = sum(ord(x) for x in input()) // i

    if ascii_sum % 2 != 0:
        odds.add(ascii_sum)
    else:
        evens.add(ascii_sum)

if sum(odds) == sum(evens):
    print(", ".join(map(str, odds.union(evens))))
elif sum(odds) > sum(evens):
    print(", ".join(map(str, odds.difference(evens))))
else:
    print(", ".join(map(str, odds.symmetric_difference(evens))))
