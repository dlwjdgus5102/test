# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 합을 출력하세요.
# 단, sum() 함수는 사용하지 마세요.

n = [1, 2, 3, 4, 5]
total = 0

for number in n:
    total = total + number

print(total)