def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if arr[-1] < divisor: break
        if i % divisor == 0: answer.append(i)
    if answer == []: answer.append(-1)

    print(answer)
    return answer

if __name__ == "__main__":
    solution([5, 9, 7, 10],5)
    solution([2, 36, 1, 3],1)
    solution([3,2,6],10)