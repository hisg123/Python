def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    #n_list = [1, 2, 3, 4, 5]
    n_list = []
    for i in range(n):
        n_list.append(i+1)

    ##n_list = [2, 0, 2, 0, 2] #lost = [2, 4] #reverse = [1, 3, 5]
    for i in range(n):
        n_list[i] = 1
        for j in range(len(lost)):
            if i+1 == lost[j]:
                n_list[i] -= 1

        for j in range(len(reserve)):
            if i+1 == reserve[j]:
                n_list[i] += 1

    #체육복 빌리는 과정
    for i in range(n):
        if n_list[i] == 0:
            #인덱스가 0일때
            if i == 0:
                if n_list[i+1] == 2:
                    n_list[i+1] -= 1
                    n_list[i] += 1

            #인덱스가 마지막일때
            if i == n-1:
                if n_list[i-1] == 2:
                    n_list[i - 1] -= 1
                    n_list[i] += 1

            #인덱스가 중간이고 이전 숫자가 2일때, 뒤에는 0->1되면 더 안 더해주도록 처리
            if i!=0 and n_list[i-1] == 2 and n_list[i] == 0:
                n_list[i-1] -= 1
                n_list[i] += 1

            #인덱스가 중간이고 다음 숫자가 2일때,
            if i!=n-1 and n_list[i+1] == 2 and n_list[i] == 0:
                n_list[i+1] -= 1
                n_list[i] += 1

    for n_number in n_list:
        if n_number >= 1:
            answer += 1

    return answer


if __name__ == '__main__':
    solution(5, [2,4,5], [1, 3])
    solution(5, [2,4], [1,3,5])
    solution(5, [2, 4], [3])
    solution(3, [3], [1] )
    solution(10, [8,10],[6,7,9])
    solution(10, [5,4,3,2,1], [3,1,2,5,4])
