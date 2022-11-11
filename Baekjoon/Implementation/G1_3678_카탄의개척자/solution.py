def solution():
    c = int(input())
    tile = {1:1} # tile[i] : i번 타일의 자원
    adj_tiles = {1:set([2,3,4,5,6,7])} # tile[i] : i번 타일과 인접한 타일

    for i in range(2, 8): # 1번 타일부터 초기화할 때, 2~7번 타일이 1번 타일과 인접한다는 것을 알 수 있음
        adj_tiles[i] = set([1])

    inputs = [int(input()) for _ in range(c)]
    max_n = max(inputs)

    resource = [[1, 1], [2, 0], [3, 0], [4, 0], [5, 0]] # [자원 번호, 나타난 횟수]

    for i in range(2, max_n+1):
        if i in adj_tiles:
            adj_tiles[i].add(i-1)
            adj_tiles[i].add(i+1)
            
            # 인접한 타일은 총 6개
            # 이전 타일의 인접 타일 중 가장 번호가 큰 타일부터 시작 1씩 더해진 타일
            # (총 6개가 될때까지) 
            # ex)
            # 1번 인접 타일: 2, 3, 4, 5, 6, 7 (초기화)
            # 2번 인접 타일: 1, 3, 7, 8, 9, 10
            # 3번 인접 타일: 1(1번의 인접 타일을 구할 때 추가됨), 2, 4(앞 뒤 타일), 10, 11, 12(2번 인접 타일 중 가장 번호가 큰 타일부터 타일 개수가 총 6개가 될 때까지의 번호)
            pre_max_adj =  max(adj_tiles[i-1])
            remain_cnt = 6 - len(adj_tiles[i])
            for j in range(pre_max_adj, pre_max_adj + remain_cnt):
                adj_tiles[i].add(j)
                if j in adj_tiles: # j의 인접 타일에도 i를 추가
                    adj_tiles[j].add(i)
                else:
                    adj_tiles[j] = set([i])
        
        resource.sort(key=lambda x:(x[1], x[0])) # 가장 적게 나타난 자원부터, 번호가 작은 것부터

        can_select = [True, True, True, True, True, True] # can_select[i] : i번 자원을 선택할 수 있는지
        
        for adj in adj_tiles[i]: # i번 자원을 선택한 인접 타일이 있다면 can_select[i] = False
            if adj in tile:
                can_select[tile[adj]] = False

        for idx, v in enumerate(resource):
            if can_select[v[0]]:
                tile[i] = v[0]
                resource[idx][1] += 1
                break
    
    for n in inputs:
        print(tile[n])


if __name__ == "__main__":
    solution()