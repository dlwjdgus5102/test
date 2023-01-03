# 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.

n = int(input('정수를 입력하세요 >'))

if n > 0 and n%2 == 0:
    print(True)
else:
    print(False)
