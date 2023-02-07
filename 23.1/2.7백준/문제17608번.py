from sys import stdin

n = int(input())
data = [0]*n
for i in range(0,n) :
    data[i] = int(stdin.readline())

    
curBig = 0
count = 0

for i in range(1,n+1) :
    if data[-i] > curBig :
        curBig = data[-i]
        count+=1
      
print(count)