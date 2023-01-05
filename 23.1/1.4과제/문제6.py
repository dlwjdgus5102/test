# 양의 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.
# 단, max() 함수는 사용하지 마세요.

n = [1, 2, 5, 4, 3]
max_value = 0
for number in n:
    if number > max_value:
        max_value = number
print(max_value)
