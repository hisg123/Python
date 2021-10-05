def DFS(numbers, target, depth):
    if depth == len(numbers):
    else:
        if numbers[depth]:

    depth += 1


def solution(numbers, target):
    answer = 0
    depth = 0
    answer = DFS(numbers, target, depth)
    print(answer)
    return answer

if __name__ == '__main__':
    solution([1, 1, 1, 1, 1], 3)
    solution([1, 1, 1, 1, 1, 1], 2)
    solution([3, 2, 1, 5, 4], 5)