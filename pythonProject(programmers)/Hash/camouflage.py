from collections import defaultdict
def solution(clothes):
    answer = 0
    p = defaultdict(list)

    for cloth in clothes:
        p[cloth[1]].append(cloth[0])

    if len(p) == 1:
        answer = len(p[clothes[0][1]])

    else:
        temp = 1
        for key in p.keys():
            temp *= len(p[key])+1
        answer += temp - 1

    return answer

if __name__ == '__main__':
    solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["sunglasses", "eyewear"], ["green_turban", "headgear"],
              ["blond","hair"], ["black","hair"]])

    solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
