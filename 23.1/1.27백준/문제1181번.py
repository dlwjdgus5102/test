n = int(input())
str_list = []
for i in range(n):
    str_list.append(input())
str_new_list = list(set(str_list))
str_new_list.sort(kye= lambda x :(len(x),x))

for j in str_new_list:
    print(j)