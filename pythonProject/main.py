
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        slice=array[i-1:j]
        sort(slice)
        answer.append(slice[k-1])

    print(answer)
    return answer

def sort(array):
    for array_num in array:
        for array_o_num in array:
            if array_num > array_o_num:
                temp = array_o_num
                array_num = array_o_num
                array_o_num = temp
    return array

if __name__ == '__main__':
    solution([1,5,2,6,3,7,4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
