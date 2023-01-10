T = int(input())

for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    가장큰수 = max(numbers)
    print(f"#{t} {가장큰수}")