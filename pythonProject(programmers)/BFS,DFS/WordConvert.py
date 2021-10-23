from collections import deque, defaultdict
import copy
def CalcStrSubLen(cp_word, word):
    a_list = list(cp_word)
    b_list = list(word)

    for b in b_list:
        if b in a_list:
            a_list.remove(b)

    return len(a_list)

def MakeGraph(words):
    graph = defaultdict(list)
    cp_words = copy.deepcopy(words)
    for word in words:
        for cp_word in cp_words:
            if CalcStrSubLen(cp_word, word) == 1:
                 graph[word].append(cp_word)
    print(graph)
    return graph

def DFS(begin, target, graph):
    visited = []
    stack = deque([begin])

    step = 0
    while stack:
        if target in stack:
            visited.append(target)
            step += 1
            break
        else: n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
            step += 1
            if visited[-1] == target: break
    print(visited)

    visited = []
    stack = deque([begin])
    step_r = 0
    while stack:
        if target in stack:
            visited.append(target)
            step_r += 1
            break
        else:
            n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack.extend(reversed(graph[n]))
            step_r += 1
            if visited[-1] == target: break

    print(visited)
    return min(step_r, step) - 1

def solution(begin, target, words):
    if target not in words:
        answer = 0
        print(answer)
        return answer

    words.append(begin)
    graph = MakeGraph(words)
    answer = DFS(begin, target, graph)

    print(answer)
    return answer

if __name__ == '__main__':
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "cog"])
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    solution("hit", "lzt", ["hot", "dot", "dog", "lot", "zot", "lzt"])