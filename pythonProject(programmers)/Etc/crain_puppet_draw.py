def solution(board, moves):
    answer = 0
    ans_list = []
    temp = [[0 for col in range(len(board))] for row in range(len(board))]

    ##inverse row and column
    for i in range(len(board)):
        for j in range(len(board)):
            temp[i][j] = board[j][i]

    #execute draw by moves array
    for i in range(len(moves)):
        # print(move)
        for j in range(len(board)):
            if temp[moves[i]-1][j] != 0:
                ans_list.append(temp[moves[i] - 1][j])
                temp[moves[i]-1][j] = 0
                break

    n = len(ans_list)
    print(ans_list)

    #pop if the same doll(repair)
    i = 0
    while(1):
        if ans_list[i] == ans_list[i+1]:
            ans_list.pop(i)
            ans_list.pop(i)
            i = -1

        i = i+1
        if i == len(ans_list)-1: break
        if ans_list == []:
            answer = answer + 2
            break

    answer = n - len(ans_list)
    return answer

if __name__ == '__main__':
    solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
