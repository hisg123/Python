from collections import defaultdict

def solution(clothes):
    answer = 0
    p = defaultdict(list)
    clothes_type = []

    for cloth in clothes:
        p[cloth[1]].append(cloth[0])
        clothes_type.append(cloth[1])
    #중복제거
    clothes_type = list(set(clothes_type))

    if len(p) == 1:
        answer = len(p[clothes_type[0]])

    else:
        temp = 1
        for cloth_type in clothes_type:
            temp *= len(p[cloth_type])+1
        answer += temp - 1
    print(answer)
    return answer

if __name__ == '__main__':
    solution([["yellowhat", "headgear"],
              ["bluesunglasses", "eyewear"],
              ["sunglasses", "eyewear"],
              ["green_turban", "headgear"],
              ["blond","hair"],
              ["black","hair"]])

    solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
    solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
