from collections import deque
import sys
sys.stdin = open("input.txt", "r")


def get_distance(n, s, p, ice_block):
    dist = [0 for _ in range(n+1)]  # dist[i] : i번 얼음 블록과 펭귄의 최단 거리
    for ice in ice_block[p]:
        dist[ice] = 1               # 1. 펭귄과 맞닿은 블록과의 거리를 1로 초기화

    queue = deque(ice_block[p])     # 2. 펭귄과 얼음 블록 간의 최단 거리 구하기
    while queue:
        cur_ice = queue.popleft()

        if cur_ice <= s: continue               # 지지대 블록일 경우

        for next_ice in ice_block[cur_ice]:     # 다음으로 연결된 블록들
            if dist[next_ice]: continue         # 방문한 블록일 경우 continue
            dist[next_ice] = dist[cur_ice] + 1  # 펭귄과의 거리 기록
            queue.append(next_ice)

    return dist[1:s+1]              # 3. 지지대 블록과 펭귄의 최단 거리 반환


def get_cnt(n, dist):
    # 펭귄과 가장 가까운 지지대 2개 사이에 있는 블록을 제외한 얼음 블록을 깰 수 있음
    dist.sort()
    return n - (dist[0] + dist[1] + 1)


def main():
    n, s, p = map(int, input().split())
    ice_block = {i:[] for i in range(1, n+1)}   # 연결 리스트

    for _ in range(n-1):
        a, b = map(int, input().split())
        ice_block[a].append(b)
        ice_block[b].append(a)

    dist = get_distance(n, s, p, ice_block) # 1. 지지대 블록과 펭귄 간의 거리를 구함
    max_cnt = get_cnt(n, dist)              # 2. 펭귄을 떨어트리지 않고 깰 수 있는 얼음의 최대 개수를 구함
    print(max_cnt)


if __name__ == "__main__":
    main()