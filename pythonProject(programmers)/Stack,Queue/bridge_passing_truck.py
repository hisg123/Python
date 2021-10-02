from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)
    sum_bridge = 0

    #bridge 배열이 []가 될때까지 반복
    while bridge:
        #만약 truck이 bridge에 들어갈 수 있는 상태라면
        if truck_weights and sum_bridge + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            sum_bridge += truck
            bridge.append(truck)

            temp = bridge.popleft()
            sum_bridge -= temp

        #truck이 bridge에 들어갈 수 없는 상태라면
        else:
            temp = bridge.popleft()
            sum_bridge -= temp

            #만약 truck_weights 배열이 []가 아니라면
            if truck_weights:
                #하나 팝하자마자 바로 드갈 수 있는 상태라면
                if sum_bridge + truck_weights[0] <= weight:
                    truck = truck_weights.popleft()
                    sum_bridge += truck
                    bridge.append(truck)
                
                #하나 팝해도 바로 드갈 수 있는 상태가 아니라면
                else: bridge.append(0)

        answer += 1
        print(sum_bridge, bridge)

    print(answer)
    return answer

if __name__ == '__main__':
    solution(2, 10, [7,4,5,6])
    solution(100, 100, [10])
    solution(100, 100, [10,10,10,10,10])
    solution(2, 10, [7,3,5,6])