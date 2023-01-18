t = list(map(int, input().split()))
a = [1, 2, 3, 4, 5]

while True:
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            t[i], t[i+1] = t[i+1], t[i]
            print(" ".join(map(str, t)))

    if t == a:
        break