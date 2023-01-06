string = input("문자열을 입력하세요 > ")
count = 0
for char in string:
    if (
        char == "e"
        or char == "E"
        or char == "a"
        or char == "A"
        or char == "i"
        or char == "I"
        or char == "o"
        or char == "O"
        or char == "u"
        or char == "U"
    ):
        count += 1

print(count)