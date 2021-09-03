def solution(name):
    answer = 0
    name_list = list(name)
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    X_idx = [i for i in range(len(name_list)) if not 'A' in name_list[i]]
    A_idx = [i for i in range(len(name_list)) if 'A' in name_list[i]]

    for i in name_list:
        answer += min(alphabet.index(i), 25 - alphabet.index(i) + 1)

    if A_idx == []:
        answer += X_idx[-1]
        return answer

    if X_idx == []:
        return answer

    if A_idx[-1] > X_idx[-1]:
        answer += min(X_idx[-1], A_idx[-1] - X_idx[0] + 1)
        return answer

    if A_idx[-1] < X_idx[-1]:
        if A_idx[0] >= 2 and A_idx[0] + len(A_idx) - 1 == A_idx[-1]:
            answer += min(X_idx[-1], len(X_idx))
            return answer
        else:
            answer += min(X_idx[-1], X_idx[-1] - X_idx[1] + 1)
            return answer

if __name__ == '__main__':
    print(
        solution("JEROEN")
        ,solution("JAEAE")
        ,solution("JAN")
        ,solution("JAZ")
        ,solution("AAABBA")
        ,solution("ZZAAAAZZ")
        ,solution("BBBAAAB")
        ,solution("ABABAAAAABA"))