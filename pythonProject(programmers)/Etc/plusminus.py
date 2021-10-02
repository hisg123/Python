def solution(absolutes, signs):

    answer = sum(absolutes)
    for i in range(len(signs)):
        if signs[i] == False:
            answer -= absolutes[i]*2

    print(answer)
    return answer

if __name__ == '__main__':
    solution([4,7,12], [True, False, True])
    solution([1,2,3], [False, False, True])