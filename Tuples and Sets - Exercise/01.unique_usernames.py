n = int(input())
names = set()

for _ in range(n):
    username = input()
    names.add(username)

for name in names:
    print(name)            # print(*names, sep="\n")


# print(*{input for _ in range(int(input)))}, sep = '\n')
