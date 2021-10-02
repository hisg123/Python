def solution(participant, completion):
    p = dict()
    hash_sum = 0

    for i in participant:
        p[hash(i)] = i
        hash_sum += hash(i)

    for i in completion:
        hash_sum -= hash(i)

    answer = p[hash_sum]
    return answer

if __name__ == '__main__':
    solution(["leo", "kiki", "eden"],["eden", "kiki"])
    solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])