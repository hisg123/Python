def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice=array[i-1:j] #j는 -1 안해주는 이유는 끝에 하나를 안쳐준다.
        slice.sort()
        answer.append(slice[k-1])
    return answer

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

if __name__ == '__main__':
    solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
