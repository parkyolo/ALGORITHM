from collections import deque

def main():
    _, w, L = map(int, input().split())
    trucks = deque(list(map(int, input().split()))) # 남은 트럭
    bridge = deque([0 for _ in range(w)]) # 다리 위의 상태
    weight = 0 # 다리 위 트럭의 무게
    sec = 0 # 걸린 시간
    while trucks:
        sec += 1
        truck = trucks.popleft()
        weight -= bridge.popleft()
        if weight + truck <= L: # 트럭이 다리 위에 올라갈 수 있으면
            bridge.append(truck)
            weight += truck
        else: # 올라갈 수 없으면
            trucks.appendleft(truck)
            bridge.append(0)
    
    sec += w # 마지막 트럭이 다리를 건너는 시간
    print(sec)
        

if __name__ == "__main__":
    main()