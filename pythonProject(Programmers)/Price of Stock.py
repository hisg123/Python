def solution(prices):
    answer = []

    cnt = 0

    while(len(prices) != 0):
        temp = prices.pop(0)
        i = 0
        print(i, temp, prices, answer)

        if prices[i] < temp:
            answer.append(cnt)
            i+=1
            cnt = 0

        else:
            cnt +=1
            i+=1

    return answer

if __name__ == '__main__':
    solution([1, 2, 3, 2, 3])
