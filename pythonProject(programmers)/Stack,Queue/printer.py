def solution(priorities, location):
    cnt = 0

    while(len(priorities)!=0):
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
            return answer

# def solution2(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer

if __name__ == '__main__':
    solution([2,1,3,2], 2)


