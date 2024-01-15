n, m = map(int, input().split())  # [int(x) for x in input().split()]
set_n = set()                     # {input() for _ in range(n)}
set_m = set()                     # {input() for _ in range(m)}


for _ in range(n):
    set_n.add(int(input()))
for _ in range(m):
    set_m.add(int(input()))

intersection_set = set_n & set_m

print(*intersection_set, sep="\n")    # print(*set_n.intersection(set_m), sep=\n)

