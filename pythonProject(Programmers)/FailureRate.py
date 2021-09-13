def solution(N, stages):
    answer = []
    FRbyStage = dict()
    denom = len(stages)

    for i in range(1, N+1):
        moleclue = stages.count(i)
        #if no one reached i-stage
        if denom == 0: FRbyStage[i] = 0
        else:
            FRbyStage[i] = moleclue/denom
            # print(moleclue, denom, FRbyStage)
            denom -= moleclue

    #sort by dict(hash)_value
    FRbyStage = sorted(FRbyStage.items(), key=lambda value: value[1], reverse=True)
    for key,value in FRbyStage: answer.append(key)
    # print(answer)
    return answer

if __name__ == "__main__":
    solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
    solution(4, [4,4,4,4,4])
    solution(2, [1,1,1,1,1])