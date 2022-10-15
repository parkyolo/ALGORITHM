from collections import deque

n, board = 0, []
area, population = [], []

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
min_diff = 0

# 경계선을 5번 선거구로 표시하는 함수
def make_boundary(x, y, d1, d2): 
    for i in range(d1+1):
        area[x+i][y-i] = 5
    for i in range(d2+1):
        area[x+i][y+i] = 5
    for i in range(d2+1):
        area[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        area[x+d2+i][y+d2-i] = 5

# 좌표와 (x, y, d1, d2)의 정보로 해당 좌표의 선거구 번호를 반환하는 함수
def get_number(r, c, x, y, d1, d2): 
    if 1 <= r < x+d1 and 1 <= c <= y:
        return 1
    elif 1 <= r <= x+d2 and y < c <= n:
        return 2
    elif x+d1 <= r <= n and 1 <= c < y-d1+d2:
        return 3
    elif x+d2 < r <= n and y-d1+d2 <= c <= n:
        return 4

# 좌표마다 선거구 번호를 매기는 함수
def numbering(x, y, d1, d2): 
    start_point = [[1, 1] , [1, n], [n, 1], [n, n]] # 4개의 끝점에서 선거구가 시작됨
    for i, point in enumerate(start_point):
        r, c = point
        queue = deque([[r, c]])
        number = i+1 # 선거구 번호
        area[r][c] = number
        while queue:
            cr, cc = queue.popleft()
            for d in range(4):
                nr, nc = cr + dxy[d][0], cc + dxy[d][1]
                if nr < 1 or nr > n or nc < 1 or nc > n: continue       # 범위를 벗어나면 continue
                if area[nr][nc] != 0: continue                          # 경계선이면 continue
                if get_number(nr, nc, x, y, d1, d2) != number: continue # 다른 선거구이면 continue
                area[nr][nc] = number
                queue.append([nr, nc])

# 선거구 별 인구수를 세는 함수
def count_population(): 
    for r in range(1, n+1):
        for c in range(1, n+1):
            if area[r][c] == 0: # 경계선 안은 5번 선거구
                population[5] += board[r][c]
            else:
                population[area[r][c]] += board[r][c]

# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이를 반환하는 함수
def get_diff(): 
    return max(population[1:]) - min(population[1:])

def main():
    global n, board, min_diff, area, population
    n = int(input())
    board = [[0 for _ in range(n+1)]] + list([0]+list(map(int, input().split())) for _ in range(n))
    min_diff = sum([sum(line) for line in board])

    # d1, d2 >= 1
    # 1 <= x < x+d1+d2 <= N
    # 1 <= y-d1 < y < y+d2 <= N
    for d1 in range(1, n):
        for d2 in range(1, n):
            for x in range(1, n-d1-d2+1):
                for y in range(1+d1, n-d2+1):
                    area = [[0 for _ in range(n+1)] for _ in range(n+1)] # 1. 선거구 번호, 인구 초기화
                    population = [0 for _ in range(6)]                      
                    make_boundary(x, y, d1, d2)                          # 2. 경계선 만들기
                    numbering(x, y, d1, d2)                              # 3. 1~4번 선거구 번호 매기기
                    count_population()                                   # 4. 선거구 별 인구 수 세기
                    diff = get_diff()                                    # 5. 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이 구하기
                    min_diff = min(min_diff, diff)                       # 6. 인구 차이의 최솟값 갱신

    print(min_diff)

if __name__ == "__main__":
    main()