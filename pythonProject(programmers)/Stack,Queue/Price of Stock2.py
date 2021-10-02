from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while (len(prices) != 0):
        temp = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if i < temp: break

        answer.append(cnt)
    return answer

if __name__ == '__main__':
    solution([1, 2, 3, 2, 3])
    solution([3,1,1])
