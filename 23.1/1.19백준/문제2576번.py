n = []
for i in range(7):
    a = int(input())
    if a % 2 == 0:
        continue
    else:
        n.append(a)
if len(n) == 0:
    print(-1)
else:
    print(sum(n),min(n),sep="\n")