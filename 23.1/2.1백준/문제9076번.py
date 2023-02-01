def score_aggregation(scores):
    scores.remove(max(scores))
    scores.remove(min(scores))
    
    if max(scores) - min(scores) > 3:
        answer = "KIN"
    else:
        answer = sum(scores)
        
    return answer

if __name__ == "__main__":
    for _ in range(int(input())):
        scores = list(map(int, input().split()))
        print(score_aggregation(scores))