def main():
    board = list(list(map(int, input().split())) for _ in range(10))
    
    state = [['.' for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if board[i][j] == 100: # 100번째 라운드에 # 고정
                state[i][j] = '#'

    # '#' 4척, '##' 3척, '###' 2척, '####' 1척이 좌우, 상하, 대각선으로 인접하지 않아야 함
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    def can_arrange(x, y):
        if x < 0 or x > 9 or y < 0 or y > 9: return False
        for d in range(8):
            nx, ny = x+dxy[d][0], y+dxy[d][1]
            if nx < 0 or nx > 9 or ny < 0 or ny > 9: continue
            if state[nx][ny] == '#': return False
        return True

    
    remain = [0, 3, 3, 2, 1] # remain[i] : 놓아야 하는 i 칸 크기의 전함 개수

    for i in range(10):
        for j in range(10):
            if state[i][j] == '#': continue

            for r in range(4, 0, -1): # 4칸짜리 전함부터 배치

                if remain[r] == 0: continue # r칸짜리 전함이 남아있지 않다면 continue

                arranged = True # 전함을 놓을 수 있으면 True

                # r칸짜리 전함을 가로로 배치
                for s in range(r):
                    if not can_arrange(i, j+s): arranged = False

                if arranged:
                    for s in range(r):
                        state[i][j+s] = '#'
                    remain[r] -= 1
                    break

                # r칸짜리 전함을 세로로 배치
                arranged = True
                for s in range(r):
                    if not can_arrange(i+s, j): arranged = False

                if arranged:
                    for s in range(r):
                        state[i+s][j] = '#'
                    remain[r] -= 1
                    break

    for s in state:
        print(''.join(s))


if __name__ == "__main__":
    main()