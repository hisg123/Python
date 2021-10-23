from collections import deque, defaultdict
def MakeGraph(tickets):
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for key, value in graph.items():
        value.sort(reverse=True)
    return graph

def DFS(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])

    answer = visited
    return answer

def solution(tickets):
    graph = MakeGraph(tickets)
    print(graph)
    answer = DFS(graph, tickets[0][0])
    print(answer)
    return answer

if __name__ == '__main__':
    # solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
