def solution(n, costs):
    
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda x:x[2])
    
    # 연결된 섬을 저장하는 집합
    island = set([costs[0][0]])
    answer = 0
    
    while len(island) != n:
        for i, cost in enumerate(costs):
            if cost[0] in island and cost[1] in island:
                continue
                
            if cost[0] in island or cost[1] in island:
                island.update([cost[0], cost[1]])
                answer += cost[2]
                # 방문한 값은 -1로 바꿔줌
                costs[i] = [-1, -1, -1]
                break
        
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))