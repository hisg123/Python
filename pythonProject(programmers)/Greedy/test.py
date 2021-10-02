def solution(number, k):
    answer = ''
    num_before = {}
    num_after = {}
    for i in range(len(number[:k])):
        num_before[i] = number[:k][i]

    for i in range(len(number[k:])):
        num_after[i] = number[k:][i]

    i = 0
    while k:
        if num_before[i] < max(num_before.values()):
            del(num_before[i])
            k -= 1
        i += 1

        if i == max(num_before.keys()): break

    print(num_before, num_after, k)

    i = 0
    flag = 0
    alen = len(num_after)
    while k:
        if i == len(num_after) - 1 :
            if len(num_after) == alen:
                flag = 1
                break

            else: i = 0

        if num_after[i] < num_after[i+1]:
            del(num_after[i])
            k -= 1
        i += 1

    i = alen - 1
    if flag == 1:
        while k:
            del(num_after[])
    print(num_before, num_after, k )
    return answer


if __name__ == '__main__':
    solution("1924", 2)
    solution("1231234", 3)
    solution("4177252841", 4)
    # solution("19763", 2)
    # solution("87654321", 3)
    solution("99999111", 3)
    # solution("1111", 3)
    # solution("8999", 3)
    # solution("9999991", 1)
    # solution("00000000",3)
    # solution("11111112", 3)
    # solution("0000001", 3)
    # solution("3322993843984398", 4)
    # solution("8892299221", 3)
    # solution("12345678901234567890", 19)
    # solution("01010", 3)
    # solution("559913", 2)
    # solution("9191919",1)
    # solution("00100", 2)
    # solution("010", 0)
    # solution("1111", 2)
    # solution("10000",2)
    # solution("1000100011", 5)
