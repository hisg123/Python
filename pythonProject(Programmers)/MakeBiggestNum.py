from collections import deque
def solution(number, k):
    answer = ''
    num_dict = {}
    temp = []
    for i in range(len(number)):
        num_dict[i] = number[i]

    max_pos = sorted(num_dict.items(), key=lambda value: value[1], reverse=True)[0]
    print(max_pos)
    print(num_dict)

    if k+1 < max_pos[0]:
        for i in range(max_pos[0]):
            temp.append((i, num_dict[i]))

        temp.sort(key=lambda value: value[1])
        while k:
            temp.pop(0)
            k -= 1

        temp.sort(key=lambda  value: value[0])
        print(temp)
        for index,i in temp:
            print(i)
            answer += i

        for index, i in num_dict.items():
            if index >= max_pos[0]: answer += i
        print(str(int(answer)))
        return str(int(answer))

    else:
        temp = sorted(num_dict.items(), key=lambda value: value[1])
        while k:
            temp.pop(0)
            k -= 1

        temp.sort(key=lambda value: value[0])
        for index, i in temp:
            print(i)
            answer += i

        print(str(int(answer)))
        return str(int(answer))

if __name__ == '__main__':
    solution("1924", 2)
    solution("1231234", 3)
    solution("4177252841", 4)
    solution("19763", 2)
    solution("87654321", 3)
    solution("99999111", 3)
    solution("1111", 3)
    solution("8999", 3)
    solution("9999991", 1)
    solution("00000000",3)
    solution("11111112", 3)
    solution("0000001", 3)
    solution("3322993843984398", 2)