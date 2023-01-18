T = int(input())

for i in range(T):
    a = list(map(list,input().split()))
    for i in a:
        print("".join(i[::-1]),end=" ")