def solution(progresses, speeds):
    answer = []
    temp_list = []

    ##calculate distribution date
    for i in range(len(progresses)):
        temp_list.append(100-progresses[i])
        if temp_list[i] % speeds[i] != 0:
            temp_list[i] = temp_list[i]//speeds[i]
            temp_list[i] +=1

        else:
            temp_list[i] = temp_list[i] // speeds[i]

    cnt = 0
    max_temp = temp_list[0]
    i = 0

    #calculate answer(=return)
    while(i!=len(temp_list)):
        if temp_list[i] <= max_temp:
            cnt += 1
            if i == len(temp_list)-1:
                answer.append(cnt)

        if temp_list[i] > max_temp:
            max_temp = temp_list[i]
            answer.append(cnt)
            cnt = 0
            i -=1

        i += 1

    return answer

if __name__ == '__main__':
    solution([93,30,55],[1,30,5])
    solution([95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1])