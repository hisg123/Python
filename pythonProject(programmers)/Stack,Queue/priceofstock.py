def solution(prices):
    answer = []
    temp = prices.pop(0)

    flag = 0
    while(prices!=[]):
        print(temp, prices, answer)
        if temp <= min(prices):
            answer.append(len(prices))

        if temp > max(prices):
            answer.append(prices.index(max(prices))+1)
            flag = 1

        if flag != 1 and temp > min(prices):
            answer.append(prices.index(min(prices))+1)
        temp = prices.pop(0)

    answer.append(0)
    print(answer)
    return answer

if __name__ == '__main__':
    solution([1,2,3,2,3])
    solution([1,1,1,1])
    solution([3,2,1])