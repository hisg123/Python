def solution(n):
    temp = n
    remainder_list = []

    ##make remainder list
    while(temp!=0):
        remainder_list.append(temp%3)
        temp = temp//3

    remainder_list.reverse()
    length = len(remainder_list)

    ##convert 124world_number
    for i in range(length-1, -1, -1):
        if i!=len(remainder_list)-1 and remainder_list[i+1] <= 0 :
            remainder_list[i] -= 1

            if remainder_list[0] == 0:
                remainder_list.remove(remainder_list[0])

    for i in range(len(remainder_list)):
        if remainder_list[i] == 0:
            remainder_list[i] = 4

        if remainder_list[i] == -1:
            remainder_list[i] = 2

    ##convert array to string
    answer = ''.join(list(map(str, remainder_list)))
    return answer

if __name__ == '__main__':
    for i in range(1, 1000):
        solution(i)
