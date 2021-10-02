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

    answer = " ".join(visited)
    return answer

def DFS(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(reversed(graph[n]))

    answer = " ".join(visited)
    return answer

N, M, V = input().split()
graph = defaultdict(list)
temp = []
for i in range(int(M)):
    a, b = input().split()
    temp.append((a,b))
    temp.append((b,a))

for key, value in temp:
    graph[key].append(value)

for key, value in graph.items():
    graph[key].sort()

print(DFS(graph, V))
print(BFS(graph, V))

