n = int(input())
a = list(map(int, input().split()))
counter = 0
for i in range(min(a), max(a)+1):
    if a.count(i) > 1:
        counter += a.count(i) - 1
print(counter)