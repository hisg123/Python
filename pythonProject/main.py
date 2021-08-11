def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice=array[i-1:j] #j는 -1 안해주는 이유는 끝에 하나를 안쳐준다.
        #slice.sort()
        sort(slice)
        answer.append(slice[k-1])
    print(answer)
    return answer

def sort(array):
    for i in range(0, len(array)): #range는 0~len(array-1)까지 뽑음 0, 1, 2, 3
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

if __name__ == '__main__':
    solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
