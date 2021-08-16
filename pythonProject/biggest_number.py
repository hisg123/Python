from itertools import permutations

def solution(numbers):
    answer_temp = ''
    temp_list = list(permutations(numbers, len(numbers)))
    answer_list = []

    for temp in temp_list:
        # print(temp, temp[0], len(temp))
        answer_temp = ''
        for i in range(len(temp)):
            answer_temp = answer_temp+str(temp[i])
        answer_list.append(int(answer_temp))
        print(answer_list)

    answer = str(max(answer_list))
    print('this is', answer)
    return answer

if __name__ == '__main__':
    solution([6, 10, 2])
    solution([3, 30, 34, 5, 9])