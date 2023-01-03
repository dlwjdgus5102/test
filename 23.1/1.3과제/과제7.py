# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요

n1 = int(input('첫 번째 정수를 입력하세요'))
n2 = int(input('두 번째 정수를 입력하세요'))

for i in range(n1, n2+1, 1):
    print(i)
if n1==n2:
    print(False)