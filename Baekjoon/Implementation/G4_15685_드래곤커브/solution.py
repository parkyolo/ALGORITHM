g = 0
grid, curve = [], []

def make_curve(x, y, g, curgen):
    if curgen > g: return

    curvelen = len(curve)
    for i in range(curvelen-2, -1, -1):
        px, py = curve[i]
        nx, ny = x+py-y, y-px+x # 90도 회전한 위치
        grid[nx][ny] = 1        # 격자에 드래곤 커브 위치 저장
        curve.append((nx, ny))  # 현재 드래곤 커브 저장

    make_curve(curve[-1][0], curve[-1][1], g, curgen+1) # 다음 세대

def main():
    global g, grid, curve

    n = int(input())
    grid = [[0 for _ in range(101)] for _ in range(101)] # grid가 1이면 드래곤 커브의 일부
    dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    for _ in range(n):
        y, x, d, g = map(int, input().split())  # 0, 편의상 x축과 y축을 반대로 저장
        nx, ny = x+dxy[d][0], y+dxy[d][1]       # 1. 0세대 드래곤 커브 생성
        grid[x][y] = 1                          # 2. 드래곤 커브의 방문 체크
        grid[nx][ny] = 1
        curve = [(x, y), (nx, ny)]              # 3. 현재 드래곤 커브의 경로 저장
        make_curve(nx, ny, g, 1)                # 4. 1~g세대 드래곤 커브 생성
    
    cnt = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]: cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()