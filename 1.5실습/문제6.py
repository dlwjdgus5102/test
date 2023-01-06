string = input("문자열을 입력하세요 > ")
dict_variable = {}
for char in string:
    if char in dict_variable.keys():
        dict_variable[char] += 1
    elif char not in dict_variable.keys():
        dict_variable[char] = 1

for key, value in dict_variable.items():
    print(key, value)