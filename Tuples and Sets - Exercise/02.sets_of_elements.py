n, m = map(int, input().split())
set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(int(input()))
for _ in range(m):
    set_m.add(int(input()))

intersection_set = set_n & set_m

for num in intersection_set:
    print(num)
