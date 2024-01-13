n = int(input())

normal = set()
vip = set()

for _ in range(n):
    code = input()
    if code[0].isdigit() and code not in vip:
        vip.add(code)
    elif code not in normal:
        normal.add(code)

ticket = input()

while ticket != "END":
    if ticket[0].isdigit():
        vip.remove(ticket)
    else:
        normal.remove(ticket)
    ticket = input()

result = vip | normal
result = sorted(result)
print(len(result))
print(*result, sep="\n")
