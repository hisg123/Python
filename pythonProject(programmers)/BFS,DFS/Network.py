from collections import deque, defaultdict
def MakeGraph(n):
    graph = defaultdict(list)

    num_index = 0
    for num in n:
        index = 0
        num_index += 1
        for i in num:
            index += 1
            if i == 1:
                print(index, i)
                graph[num_index].append(index)

    print("this is graph", graph)
    return graph

def solution(n, computers):
    graph = MakeGraph(n)
    answer = 0
    print(answer)
    return answer

if __name__ == '__main__':
    solution([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2)
