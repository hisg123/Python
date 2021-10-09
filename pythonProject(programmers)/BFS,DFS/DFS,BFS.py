#baekjoon #1260
from collections import deque, defaultdict
def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
        # print(queue, graph[n], visited)

    answer = visited
    return answer

def DFS(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(reversed(graph[n]))

    answer = visited
    return answer

if __name__ == '__main__':
    graph = defaultdict(list)
    graph = {1: [2],
             2: [1,3],
             3: [2]}
    root = 1
    print(DFS(graph, root))
    #print(BFS(graph, root))

