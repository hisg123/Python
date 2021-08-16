def solution(scores):
    temp_array = []
    temp = [[0 for col in range(len(scores))] for row in range(len(scores))]
    result = ""

    ##inverse row and column
    for i in range(len(scores)):
        for j in range(len(scores)):
            temp[i][j] = scores[j][i]

    ##find if the same min or max number
    for i in range(len(temp)):
        cnt = 0

        #if temp[i][i] is max or min number
        if temp[i][i] == min(temp[i]) or temp[i][i] == max(temp[i]):
            cnt = cnt + 1

            # if not only one max or min num
            for j in range(0, len(temp)):
                if temp[i][i] == temp[i][j] and j != i:
                    cnt = 0

            # mark if temp[i][i] is only min or max number
            if cnt == 1: temp[i][i] = 101

    ##calculate average
    for i in range(len(temp)):
        cnt = 0
        sum = 0

        #if temp[i][i] is marked
        if temp[i][i] == 101:
            cnt = cnt + 1
            for j in range(len(temp)):
                sum = sum + temp[i][j]

        #else temp[i][i] is unmarked
        else:
            for j in range(len(temp)):
                sum = sum + temp[i][j]

        temp_array.append((sum-101*cnt)/(len(temp)-cnt))

    ##give grade to each average
    for i in range(len(temp_array)):
        if temp_array[i] >= 90: result = result + 'A'
        if temp_array[i] >= 80 and temp_array[i] < 90: result = result + 'B'
        if temp_array[i] >= 70 and temp_array[i] < 80: result = result + 'C'
        if temp_array[i] >= 50 and temp_array[i] < 70: result = result + 'D'
        if temp_array[i] < 50: result = result + 'F'

    return result

if __name__ == '__main__':
    solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
    solution([[50,90],[50,87]])
    solution([[70,49,90],[68,50,38],[73,31,100]])
    solution([[75, 50, 100], [75, 100, 20], [100, 100, 20]])
