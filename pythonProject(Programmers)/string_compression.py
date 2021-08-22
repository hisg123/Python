def solution(s):
    #split list
    s_list = [[] for j in range(len(s))]
    for cnt in range(1, len(s)+1):
        i = 0
        while(i < len(s)):
            s_list[cnt-1].append(s[i:i+cnt])
            i += cnt

    answer_list = []

    #compress
    c_list = [[] for j in range(len(s_list))]
    for i in range(len(s_list)):
        j = 0
        while(j != len(s_list[i])):
            k = j
            cnt = 0

            while(k != len(s_list[i])):
                if s_list[i][j] == s_list[i][k]:
                    cnt += 1

                if s_list[i][j] != s_list[i][k]:
                    break

                k +=1

            if cnt > 1:
                c_list[i].append(str(cnt)+s_list[i][j])
                j += cnt

            else:
                if j > len(s_list[i])-1 : j = len(s_list[i])-1
                c_list[i].append(s_list[i][j])
                j += 1

        # combine c_list
        temp = ""
        for c in range(len(c_list[i])):
            temp += c_list[i][c]

        answer_list.append(len(temp))

    answer = min(answer_list)
    return answer


if __name__ == '__main__':
    solution("aabbaccc")
    solution("ababcdcdababcdcd")
    solution("abcabcdede")
    solution("abcabcabcabcdededededede")
    solution("xababcdcdababcdcd")
