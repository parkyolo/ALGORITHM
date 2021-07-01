def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    total_weight = 0 # 다리를 건너는 트럭의 총 무게
    crossing_truck = [] # 다리를 건너는 트럭
    time = [] # 다리를 건너는 트럭들의 각 경과 시간

    # 대기 트럭이 모두 다리 위에 오를 때까지
    while truck_weights:
        answer += 1
        
        # while문을 한 번 돌 때마다 다리를 건너는 트럭들의 경과 시간을 + 1
        for i in range(len(time)):
            time[i] += 1
        
        # 다리를 건너는 트럭들 중 가장 먼저 다리에 오른 트럭이 다리를 다 건넜는지 검사 
        if len(time) > 0:
            if time[0] == bridge_length:
                time.pop(0)
                total_weight -= crossing_truck.pop(0)
        
        # 대기 트럭이 다리에 오를 수 있는지 검사
        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            crossing_truck.append(truck)
            total_weight += truck
            time.append(0)
            
    # 다리를 건너는 트럭이 모두 다리를 지날 때까지
    while crossing_truck:
        answer += 1

        # while문을 한 번 돌 때마다 다리를 건너는 트럭들의 경과 시간을 + 1
        for i in range(len(time)):
            time[i] += 1

        # 다리를 건너는 트럭들 중 가장 먼저 다리에 오른 트럭이 다리를 다 건넜는지 검사 
        if time[0] == bridge_length:
            time.pop(0)
            crossing_truck.pop(0)

    return answer

answer = solution(2, 10, [7,4,5,6])
print(answer) # 8