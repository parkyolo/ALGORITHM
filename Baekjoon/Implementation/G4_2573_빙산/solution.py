from collections import deque

n, m, board, berg = 0, 0, [], {}
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def melting():
    global berg

    del_list = [] # 전부 녹아서 바다가 된 빙산
    
    for key, val in berg.items():
        x, y = key

        for i in range(4):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if (nx, ny) not in berg: val -= 1   # 바다와 인접
            if val == 0:                        # 모두 녹은 경우
                del_list.append((x, y))
        
        # 빙산 높이 갱신
        berg[key] = val 
        board[x][y] = val
    
    for key in del_list:    # 모두 녹은 빙산
        del berg[key]
        board[key[0]][key[1]] = 0


def get_cnt(): # bfs로 빙산 개수 count
    global board

    berg_cnt = 0 # 빙산 덩어리 수

    for x in range(n):
        for y in range(m):

            if board[x][y]:
                berg_cnt += 1
                
                queue = deque([(x, y)])
                while queue:
                    cx, cy = queue.popleft()
                    for i in range(4):
                        nx, ny = cx + dxy[i][0], cy + dxy[i][1]
                        if board[nx][ny] == 0: continue # 이미 방문했거나 바다일 경우

                        queue.append((nx, ny))
                        board[nx][ny] = 0 # 방문 체크

    return berg_cnt


def main():
    global n, m, board, berg

    n, m = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(n))

    for x in range(n):
        for y in range(m):
            if board[x][y]:
                berg[(x, y)] = board[x][y]
    
    time = 0

    while berg:
        time += 1             # 0. 시간 경과
        melting()             # 1. 빙산이 녹는다.
        berg_cnt = get_cnt()  # 2. 빙산 덩어리 수를 센다.

        if berg_cnt >= 2:     # 3. 빙산이 두 덩어리 이상으로 분리되는 최초의 시간 출력
            print(time)
            return
        
    print(0)                  # 4. 빙산이 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않은 경우
    return
    
    
if __name__ == "__main__":
    main()