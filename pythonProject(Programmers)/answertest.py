def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    print(namespace)
    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    print(answer)
    return answer

if __name__ == '__main__':
    solution(["Enter 123 A",
              "Leave 123",
              "Enter uid1234 B",
              "Enter uid12345 C",
              "Leave uid1234",
              "Leave uid12345",
              "Enter uid123 AB",
              "Enter ABC 광우",
              "Change ABC 현주",
              "Leave ABC"])