def solution(N, stages):
    answer = []
    FRbyStage = dict()
    denom = len(stages)
    info = [0]*(N+2)

    for stage in stages:
        info[stage] +=1

    for i in range(1, N+1):
        moleclue = info[i]
        #if no one reached i-stage
        if denom == 0: FRbyStage[i] = 0
        else:
            FRbyStage[i] = moleclue/denom
            denom -= moleclue

    #sort by dict(hash)_value
    for item in sorted(FRbyStage.items(), key=lambda value: value[1], reverse=True): answer.append(item[0])
    return answer

if __name__ == "__main__":
    solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
    solution(4, [4,4,4,4,4])
    solution(2, [1,1,1,1,1])
