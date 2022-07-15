import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))
tree_info = [[deque() for _ in range(N)] for _ in range(N)] # tree_info[r][c] = deque([나무들의 나이])
for _ in range(M):
    x, y, z = map(int, input().split())
    tree_info[x-1][y-1].append(z)

land = [[5 for _ in range(N)] for _ in range(N)] # 처음에 양분은 모든 칸에 5만큼 들어있음
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer():
    for r in range(N):
        for c in range(N):
            survived_tree = deque()
            nutrient = 0
            for age in tree_info[r][c]:
                if land[r][c] >= age: # 자신의 나이만큼 양분을 먹고, 나이가 1 증가
                    land[r][c] -= age
                    survived_tree.append(age+1)
                else: # 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 죽음
                    nutrient += age // 2 # 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
            land[r][c] += nutrient
            tree_info[r][c] = survived_tree

def fall(): # 나무가 번식함
    new_tree = []
    for r in range(N):
        for c in range(N):
            for age in tree_info[r][c]:
                if age % 5 == 0: # 번식하는 나무는 나이가 5의 배수
                    for j in range(8): # 인접한 8개의 칸에 나이가 1인 나무가 생김
                        nx, ny = r+dx[j], c+dy[j]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                        new_tree.append((nx, ny))
    for r, c in new_tree:
        tree_info[r][c].appendleft(1)

def winter(): # S2D2가 땅을 돌아다니면서 땅에 양분을 추가
    for r in range(N):
        for c in range(N):
            land[r][c] += A[r][c]

for _ in range(K):
    spring_summer()
    fall()
    winter()

cnt = 0
for r in range(N): # K년이 지난 후 상도의 땅에 살아있는 나무의 개수
    for c in range(N):
        cnt += len(tree_info[r][c])

print(cnt)