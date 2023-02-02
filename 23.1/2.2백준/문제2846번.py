n = int(input())
arr = list(map(int,(input().split())))

temp = arr[0] ; sum = 0
answer = []

for i in range(1,n):
    if arr[i] - temp >0 :
        sum += arr[i]-temp
        temp = arr[i]
        
    elif arr[i] == temp or arr[i]-temp<0 : 
        answer.append(sum)
        temp = arr[i]
        sum = 0 
        
answer.append(sum) 

if len(answer) == 0 : print(0)
else : print(max(answer)) 