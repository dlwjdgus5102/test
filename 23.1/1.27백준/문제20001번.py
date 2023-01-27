start = input()
question = 0

while True:
    is_rubberduck = input()

    if is_rubberduck =='고무오리 디버깅 끝':
        break
    else:
        if is_rubberduck == '문제':
            question += 1
        elif is_rubberduck == '고무오리':
            if question == 0:
                question += 2
            else:
                question -= 1

if question == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')

    #다시보기
