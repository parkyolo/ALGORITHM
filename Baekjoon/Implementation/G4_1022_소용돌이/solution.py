board = []


def check(r1, c1, r2, c2): # boar의 모든 값이 채워지면 False 반환
    for r in range(r2-r1+1):
        for c in range(c2-c1+1):
            if board[r][c] == '':
                return True
    return False


def main():
    global board

    r1, c1, r2, c2 = map(int, input().split())
    board = [["" for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

    x, y, num, round = -r1,-c1, 1, 1    # (0, 0)의 위치: (-r1, -c1)
    length = 0

    while check(r1, c1, r2, c2):
    
        # 1. 반시계 방향으로 (x, y)가 변화하며 num 증가
        # 2. (x, y)가 범위 안에 속하면 board[x][y] = num
        # 3. board에 값을 채울 때 숫자의 최장 길이 length 갱신
        # 4. board의 모든 값이 채워지면 종료

        if 0 <= x < r2-r1+1 and 0 <= y < c2-c1+1:
            board[x][y] = str(num)
        num += 1

        if 0 <= x < r2-r1+1 and 0 <= y+1 < c2-c1+1:
            board[x][y+1] = str(num)
        y += 1
        num += 1

        for _ in range(round*2-1):
            if 0 <= x-1 < r2-r1+1 and 0 <= y < c2-c1+1:
                board[x-1][y] = str(num)
                length = max(length, len(str(num)))
            x -= 1
            num += 1

        for _ in range(round*2):
            if 0 <= x < r2-r1+1 and 0 <= y-1 < c2-c1+1:
                board[x][y-1] = str(num)
                length = max(length, len(str(num)))
            y -= 1
            num += 1
        
        for _ in range(round*2):
            if 0 <= x+1 < r2-r1+1 and 0 <= y < c2-c1+1:
                board[x+1][y] = str(num)
                length = max(length, len(str(num)))
            x += 1
            num += 1
        
        for _ in range(round*2):
            if 0 <= x < r2-r1+1 and 0 <= y+1 < c2-c1+1:
                board[x][y+1] = str(num)
                length = max(length, len(str(num)))
            y += 1
            num += 1
        
        num -= 1
        round += 1
    
    for r in range(r2-r1+1):
        for c in range(c2-c1+1):
            # 모든 숫자의 길이가 length가 되도록 왼쪽에 공백 채우기
            print(board[r][c].rjust(length, " "), end=" ")
        print()
    

if __name__ == "__main__":
    main()