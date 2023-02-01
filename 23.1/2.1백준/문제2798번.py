n,m = map(int,input().split())
numbers = list(map(int,input().split()))
#numbers = list(filter(lambda x: x <= m-2, numbers))

size = ((n * (n-1) * (n-2)) // 6) # nC3
#size = (len(numbers) * (len(numbers)-1) * (len(numbers)-2) // 6)

results = [] * size
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if i != j and i != k and j != k:
                if numbers[i] + numbers[j] + numbers[k] <= m:
                    results.append(numbers[i] + numbers[j] + numbers[k])

print(max(results))