def solution(number, k):
    #제일 작은 수 두개 제거
    num_list = list(number)
    temp = list(number)
    print(num_list)

    i = 0
    flag = 0
    while k > 0:
        if i == len(num_list)-1 and k > 0:
            flag = 1
            i=0
            num_list = temp

        if i < len(num_list)-1 and num_list[i] < num_list[i+1]:
            temp.remove(num_list[i])
            k -= 1
            if k == 0: break

        if flag == 1 and temp[0] == max(temp):
            temp.remove(temp[-1])
            k -= 1
            if k == 0: break

        i += 1

    answer = ''.join(temp)
    print(answer)
    return answer

if __name__ == '__main__':
    solution("1924", 2)
    solution("1231234", 3)
    solution("4177252841", 4)
    solution("19763", 2)
    solution("87654321", 3)
    solution("1119999911", 3)
    solution("1111", 3)
    solution("9897", 1)

