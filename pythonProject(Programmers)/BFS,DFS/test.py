def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

if __name__ == '__main__':
    solution([1, 1, 1, 1, 1], 3)
    solution([1, 1, 1, 1, 1, 1], 2)
    solution([3, 2, 1, 5, 4], 5)