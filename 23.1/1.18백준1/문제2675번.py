T = int(input())

for i in range(T):
    a, b = input().split()
    for j in b:
        print(j*int(a), end = '')
    print()

# 반복 횟수와 문자열을 string으로 입력받아 for문으로 문자열의 각 문자를 반복 횟수만큼 곱해줘 출력했다.