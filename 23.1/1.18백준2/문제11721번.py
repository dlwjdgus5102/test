N = str(input())
count = 0

for i in range(len(N)) :
    if count < 9 :
        print(N[i], end = "")
        count += 1
    elif count == 9 :
        print(N[i])
        count = 0