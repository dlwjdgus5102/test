# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요. 두 정수가 같으면 False를 출력하세요.

n1 = int(input('첫 번쩨 정수를 입력하세요 >'))
n2 = int(input('두 번쩨 정수를 입력하세요 >'))
if n1 > n2:
    print(n1)
elif n1 < n2:
    print(n2)
elif n1 == n2:
    print(False)