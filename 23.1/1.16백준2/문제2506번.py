N = int(input())
board = list(map(int,input().split()))

score = 1
totalscore = 0

for i in range(N):
    if board[i] == 1:
        totalscore += score
        score += 1
    
    else:
        board[i] == 0
        score = 1
print(totalscore)