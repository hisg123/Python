def solution(citations):
    h_index_array = []
    h_index = max(citations)

    if h_index == 0: return h_index

    while(h_index!=0):
        cnt_high = 0

        for j in range(len(citations)):
            if citations[j] >= h_index :
                cnt_high = cnt_high+1

        if cnt_high >= h_index:
            h_index_array.append(h_index)

        h_index = h_index - 1

    h_index = max(h_index_array)
    return h_index

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

if __name__ == '__main__':
    solution([3,0,6,1,5])
    solution([2,1,1,1,0])
    solution([0,1])
    solution([2,2,2])
    solution([41,42,24])
    solution([0,0,0])