n = int(input())
s = []
for i in range(0,n):
    a = int(input())
    s.append(a)
s.sort()
for j in range(len(s)):
    print(s[j])