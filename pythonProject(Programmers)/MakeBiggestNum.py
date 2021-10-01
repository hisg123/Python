def solution(number, k):
    answer = ''
    init_k =  k
    num_dict = {}
    temp = []
    for i in range(len(number)):
        num_dict[i] = number[i]

    max_pos = sorted(num_dict.items(), key=lambda value: value[1], reverse=True)[0]
    print(max_pos)
    print(num_dict)

    for i in range(max_pos[0]):
        temp.append((i, num_dict[i]))

    #value 값을 기준으로 정렬
    temp.sort(key=lambda value: value[1])
    while k:
        if temp:
            temp.pop(0)
            k -= 1

        else: break

    #다시 key(=index) 값을 기준으로 정렬
    if k == 0:
        temp.sort(key=lambda value: value[0])
        print(temp)
        for index,i in temp:
            print(i)
            answer += i

        #나머지 부분 붙이는 곳
        for index, i in num_dict.items():
            if index >= max_pos[0]: answer += i

        print(str(int(answer)))
        return str(int(answer))

    else:
        for index, i in num_dict.items():
            if index >= max_pos[0]:
                temp.append((index,i))

        temp_dict = {}
        for key, value in temp:
            temp_dict[key] = value
        print(temp_dict)

        i = init_k - k
        while k:
            if i == len(number)-1:
                while k:
                    del(temp_dict[-1])
                    k -= 1
            if k == 0: break

            if temp_dict[i] < temp_dict[i+1]:
                del(temp_dict[i])
                k -=1
            i += 1
        print(temp_dict)

        for index, i in temp_dict.items():
            answer += i
        print(str(int(answer)))
        return str(int(answer))

if __name__ == '__main__':
    # solution("1924", 2)
    # solution("1231234", 3)
    # solution("4177252841", 4)
    solution("19763", 2)
    # solution("87654321", 3)
    # solution("99999111", 3)
    # solution("1111", 3)
    # solution("8999", 3)
    # solution("9999991", 1)
    # solution("00000000",3)
    # solution("11111112", 3)
    # solution("0000001", 3)
    # solution("3322993843984398", 2)
    # solution("8892299221", 3)



