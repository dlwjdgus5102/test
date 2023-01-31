N = int(input())
for i in range(N, 0, -1):
    value = "*" * i
    print (value.rjust(N, ' '))