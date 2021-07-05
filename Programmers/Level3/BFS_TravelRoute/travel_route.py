from collections import deque

def solution(tickets):
    answer = []

    queue = deque()
    indexes = [] # 도시를 방문하는 경로(index)를 저장하는 변수
    
    # "ICN"으로 시작하는 항공권의 index를 저장
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            queue.append([i])
    
    while queue:
        index = queue.popleft()
        ticket = tickets[index[-1]] # 해당 index의 항공권을 저장하는 변수

        # 모든 항공권을 사용했을 때 indexes 변수에 넣음
        if len(index) == len(tickets):
            indexes.append(index)
        # 모든 도시를 방문할 수 없는 경우
        elif len(index) > len(tickets):
            break
        
        for i in range(len(tickets)):
            # 사용하지 않은 항공권이면서 경로가 이어질 때
            if (i not in index) and (ticket[1] == tickets[i][0]):
                # 해당 항공권을 index에 추가하여 queue에 넣음
                queue.append(index + [i])

    # i : 방문하는 공항 경로의 index
    for i in indexes:
        # 해당 index의 공항 이름을 result에 넣음
        result = []
        for j in i:
            result.append(tickets[j][0])
        result.append(tickets[i[-1]][1])
        # answer : 모든 가능한 경로가 담겨있는 변수
        answer.append(result)
    
    # answer을 sort하여 알파벳 순서가 앞서는 경로를 return
    answer.sort()

    return answer[0]

answer = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(answer) #["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]