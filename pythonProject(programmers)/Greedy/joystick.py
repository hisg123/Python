def solution(name):
    answer = 0
    name_list = list(name)
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    X_idx = [i for i in range(len(name_list)) if not 'A' in name_list[i]]
    A_idx = [i for i in range(len(name_list)) if 'A' in name_list[i]]

    for i in name_list:
        answer += min(alphabet.index(i), 25 - alphabet.index(i) + 1)
        print(i, answer)

    if A_idx != [] and A_idx[-1] > X_idx[-1]: answer += min(X_idx[-1], A_idx[-1] - X_idx[0] + 1)
    else: answer += min(X_idx[-1], X_idx[-1] - X_idx[1] + 1)
    print(name_list, answer)
    return answer

if __name__ == '__main__':
    solution("JEROEN")
    solution("JAEAE")
    solution("JAN")
    solution("JAZ")
    solution("AAABBA")
    solution("ZZAAAZZ")