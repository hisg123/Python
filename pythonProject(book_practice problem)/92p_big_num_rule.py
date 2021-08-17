def solution(nmk, list):
    result = 0
    list.sort(reverse=True)
    print(list)
    cnt = nmk[2]
    for i in range(nmk[1]):
        if cnt !=0:
            result = result + list[0]

        else:
            result = result + list[1]
            cnt = nmk[2]

        cnt = cnt - 1

        print(result, cnt, i)

    print(result)
    return result

if __name__ == '__main__':
    solution([5,8,3],[2,4,5,4,6])
    solution([5,7,2], [3,4,3,4,3])