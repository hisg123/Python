from collections import deque, defaultdict
def MakeGraph(computers, n):
    graph = defaultdict(list)

    # [1,1,0] -> 1: [1, 2]
    for n_idx in range(n):
        computer_index = 0
        for computer in computers[n_idx]:
            computer_index += 1
            if computer == 1:
                graph[n_idx+1].append(computer_index)

    #1: [1,2] -> 1: [2]
    for key, value in graph.items():
        for v in value:
            if key ==  v: value.remove(v)

    return graph

def DFS(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(reversed(graph[n]))

    visited.sort()
    print(f"visted[root = {root}]", visited)
    answer = ''.join(str(visited))
    return answer

def solution(n, computers):
    #convert computers array to usable graph
    graph = MakeGraph(computers, n)
    print("graph:", graph)

    #do DFS by changing root
    temp = []
    for n_idx in range(n):
        root = n_idx + 1
        temp.append(DFS(graph, root))

    #delete repetive elements
    set_temp = set(temp)
    answer = len(list(set_temp))
    print(answer)
    return answer

if __name__ == '__main__':
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])