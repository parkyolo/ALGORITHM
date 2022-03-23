n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)] # di, si

rain_cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
direc = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diag = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

for d, s in move:
    for idx, cloud in enumerate(rain_cloud): # 구름이 이동하고 비가 1씩 내림
        nx, ny = ((cloud[0]+s*direc[d][0])+n)%n, ((cloud[1]+s*direc[d][1])+n)%n
        rain_cloud[idx] = (nx, ny)
        grid[nx][ny] += 1

    for cx, cy in rain_cloud: # 물복사버그
        for i in range(4):
            if 0 <= cx+diag[i][0] < n and 0 <= cy+diag[i][1] < n:
                if grid[cx+diag[i][0]][cy+diag[i][1]]:
                    grid[cx][cy] += 1

    next_cloud = []
    for i in range(n): # 구름 생성
        for j in range(n):
            if grid[i][j] >= 2 and (i,j) not in rain_cloud:
                grid[i][j] -= 2
                next_cloud.append((i,j)) 

    rain_cloud = next_cloud

print(sum([sum(line) for line in grid]))