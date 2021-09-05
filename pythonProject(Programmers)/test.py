def solution(record):
    answer = []
    COMMAND_LIST = []
    UID_LIST = []
    NAME_LIST = []

    for i in record:
        temp = i.split()
        COMMAND_LIST.append(temp[0])
        UID_LIST.append(temp[1])
        if len(temp) == 3: NAME_LIST.append(temp[2])
        else: NAME_LIST.append("")
    print(COMMAND_LIST, UID_LIST, NAME_LIST)

    IDX = 0
    for i in UID_LIST:
        UID_IDX = list(filter(lambda x: UID_LIST[x] == i, range(len(UID_LIST))))
        Enter_IDX = list(filter(lambda x: COMMAND_LIST[x][0] == 'E', UID_IDX))
        Leave_IDX = list(filter(lambda x: COMMAND_LIST[x][0] == 'L', UID_IDX))
        Change_IDX = list(filter(lambda x: COMMAND_LIST[x][0] == 'C', UID_IDX))
        print(IDX, UID_IDX, Enter_IDX, Leave_IDX, Change_IDX)
        if UID_IDX[-1] in Enter_IDX: NAME_LIST[IDX] = NAME_LIST[Enter_IDX[-1]]
        if UID_IDX[-1] in Leave_IDX:
            if Change_IDX != []: NAME_LIST[IDX] = NAME_LIST[max(Enter_IDX[-1], Change_IDX[-1])]
            else: NAME_LIST[IDX] = NAME_LIST[Enter_IDX[-1]]
        if UID_IDX[-1] in Change_IDX: NAME_LIST[IDX] = NAME_LIST[Change_IDX[-1]]
        IDX += 1
    print(COMMAND_LIST, UID_LIST, NAME_LIST)

    for i in range(IDX):
        if COMMAND_LIST[i][0] == 'E': answer.append(f"{NAME_LIST[i]}님이 들어왔습니다.")
        if COMMAND_LIST[i][0] == 'L': answer.append(f"{NAME_LIST[i]}님이 나갔습니다.")

    print(answer)
    return answer

if __name__ == '__main__':
    solution(["Enter 123 A",
              "Leave 123",
              "Enter uid1234 B",
              "Enter uid12345 C",
              "Enter 123 인기",
              "Leave uid1234",
              "Leave uid12345",
              "Enter uid123 AB",
              "Enter ABC 광우",
              "Change ABC 현주",
              "Leave ABC"])