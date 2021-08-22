def solution(s):
    answer = 0

    #split list
    s_list = [[] for j in range(len(s))]
    for cnt in range(1, len(s)+1):
        i = 0
        while(i < len(s)):
            s_list[cnt-1].append(s[i:i+cnt])
            i += cnt

    #compress
    c_list = [[] for j in range(len(s_list[i]))]
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            # for k in range(j, len(s_list[i])-j):
            k = j
            cnt = 0
            while k != len(s_list[i]):
                print(i, j, k, cnt, s_list)
                if s_list[i][j] == s_list[i][k]:
                    cnt +=1

                if s_list[i][j] != s_list[i][k]:
                    c_list[i].append(str(cnt)+s_list[i][j])
                    s_list[i][k-1] = '0'
                    break

                k += 1

    print(s_list)
    print(c_list)
    return answer


if __name__ == '__main__':
    solution("aabbaccc")
    # solution("ababcdcdababcdcd")
    # solution("abcabcdede")
    # solution("abcabcabcabcdededededede")
    # solution("xababcdcdababcdcd")
