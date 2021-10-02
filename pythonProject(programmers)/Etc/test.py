def solution(number, k):
    answer = ''
    num_dict = {}
    num_before = []
    num_after = []

    for i in range(len(number)): num_dict[i] = number[i]
    max_pos = max(num_dict, key=num_dict.get)

    # 앞대가리 손질에서 끝남
    for key, value in num_dict.items():
        if key < max_pos:
            num_before.append((key, value))
        else:
            num_after.append(value)

    num_before.sort(key=lambda value: value[1])
    while k:
        if num_before == [] and k > 0: break
        num_before.pop(0)
        k -= 1
    num_before.sort(key=lambda value: value[0])

    if k == 0:
        for key, i in num_before: answer += i
        for i in num_after: answer += i

        print(str(int(answer)))
        return answer

    # 뒷대가리까지 손질 시작
    print(num_after)

    f_len = len(num_after)
    flag = 0
    while k:
        if i == len(number)-1:
            if len(num_after) == f_len:
                flag = 1
                break
            else:
                i = 0

        if num_after[i] < num_after[i + 1]:
            num_after.pop(i)
            k -= 1
        i += 1

    # 뒷대가리 손질하다 맨마지막까지 손질 안되서 여리로 옴
    if flag == 1:
        key = 0
        temp = []
        for i in num_after:
            temp.append((key, i))
            key += 1
        temp = sorted(temp, key=lambda value: value[1])
        while k:
            temp.pop(0)
            k -= 1
        temp = sorted(temp, key=lambda value: value[0])
        for key, i in temp: answer += i
        print(str(int(answer)))
        return answer

    # 뒷대가리 손질 끝
    for i in num_after: answer += i
    print(str(int(answer)))
    return answer


if __name__ == '__main__':
    solution("1924", 2)
    solution("1231234", 3)
    solution("417725241", 4)
    solution("19763", 2)
    solution("87654321", 3)
    solution("99999111", 3)
    solution("1111", 3)
    solution("8999", 3)
    solution("9999991", 1)
    solution("00000000",3)
    solution("11111112", 3)
    solution("0000001", 3)
    solution("3322993843984398", 4)
    solution("8892299221", 3)
    solution("12345678901234567890", 19)
    solution("01010", 3)
    solution("559913", 2)
    solution("9191919",1)
    solution("00100", 2)
    solution("010", 0)
    solution("1111", 2)
    solution("10000",2)
    solution("1000100011", 5)
