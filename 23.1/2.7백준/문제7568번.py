import sys

N = int(sys.stdin.readline())
People = []
Point = [0] * N
for i in range(N):
    People.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(People)):
    for j in range(len(People)):
        if i != j:
            if People[i][0]<People[j][0] and People[i][1]<People[j][1]:
                Point[i] += 1

for i in Point:
    print(i+1, end=' ')