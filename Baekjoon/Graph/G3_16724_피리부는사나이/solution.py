def main():
    n, m = map(int, input().split())
    board = list(list(input()) for _ in range(n))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dxy = {'U':[-1, 0], 'D':[1, 0], 'L':[0, -1], 'R':[0, 1]}

    cnt = 0 # 사이클의 개수
    num = 0 # 사이클의 번호
    
    for i in range(n):
        for j in range(m):
            if visited[i][j]: continue

            # 새로운 사이클 시작
            cnt += 1
            num += 1
            x, y = i, j

            while not visited[x][y]:
                visited[x][y] = num
                x, y = x + dxy[board[x][y]][0], y + dxy[board[x][y]][1] # 다음 위치

            if visited[x][y] != num:  # 도착 지점과 번호가 다르면, 같은 사이클을 두 번 count한 것이기 때문에 사이클의 개수 -1
                cnt -= 1

    print(cnt)


if __name__ == "__main__":
    main()