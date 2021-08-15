def solution(priorities, location):
    cnt = 0

    while(len(priorities)!=0):
        print(priorities, location)
        if priorities[0] != max(priorities) and location != 0:
            priorities.append(priorities.pop(0))
            location = location - 1

        if priorities[0] != max(priorities) and location == 0:
            priorities.append(priorities.pop(0))
            location = len(priorities)-1

        if priorities[0] == max(priorities) and location != 0:
            priorities.pop(0)
            location = location - 1
            cnt = cnt+1

        if priorities[0] == max(priorities) and location == 0:
            answer = location+1+cnt
            print(answer)
            return answer

if __name__ == '__main__':
    solution([2,1,3,2], 2)
    solution([1,1,9,1,1,1], 0)

