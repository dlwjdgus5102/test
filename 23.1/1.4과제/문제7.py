# 양의 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.
# 단, min() 함수는 사용하지 마세요.

n = [5, 2, 5, 5]
min_value = n[0]
for number in n:
    if number < min_value:
        min_value = number
print(min_value)