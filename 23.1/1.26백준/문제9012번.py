t = int(input())
for _ in range(t):
    vps = str(input())
    stack = []
    check = False
    for i in range(len(vps)-1):
        if vps[i] == '(':
            stack.append('(')
        else:
            if stack:
                if stack.pop() == '(' and vps[i] == ')':
                    check = True
                else:
                    check = False
                    break
            else:
                check = False
                break
    if stack:
        check = False
    print('YES') if check else print('NO')

    # 다시보기