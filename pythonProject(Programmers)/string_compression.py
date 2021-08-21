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
    c_list = [[] for j in range(len(s))]
    for i in range(len(s_list)):
        j = 0
        while(1):
            if s_list[i][j] == s_list[i][j+1]:
                cnt +=1
                c_list[i].append(str(cnt) + s_list[i][j])
                print(j, c_list)

            else: break

    print(s_list)
    return answer


if __name__ == '__main__':
    solution("aabbaccc")
    # solution("ababcdcdababcdcd")
    # solution("abcabcdede")
    # solution("abcabcabcabcdededededede")
    # solution("xababcdcdababcdcd")
