import copy
def solution(number, k):
    origin_number = list(number)
    temp_number = list(number)
    i = 0
    while k > 0:
        # if reach last element in array
        if i == len(origin_number)-1 and k > 0:

            #if array is sorted status
            if origin_number == temp_number:
                temp_number = temp_number[:len(temp_number)-k]
                break

            else:
                i = 0
                origin_number = copy.deepcopy(temp_number)

        #defalut process
        if origin_number[i] < origin_number[i+1]:
            temp_number.remove(origin_number[i])
            k -= 1

        i += 1

    answer = "".join(temp_number)
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

