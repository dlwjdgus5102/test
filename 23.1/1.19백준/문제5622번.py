n = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for i in range(len(a)):
    for j in n:
        if a[i] in j:
            ret += n.index(j)+3
print(ret)