def moveR(x, y):    # 오른쪽으로 이동
    return x+1, y

def moveDLU(x, y):  # 대각선 왼쪽 아래로 이동
    return x-1, y+1

def moveU(x, y):    # 아래로 이동
    return x, y+1

def moveDRU(x, y):  # 대각선 오른쪽 위로 이동
    return x+1, y-1

def solution():
    x, y = 1, 1
    cnt = 1
    
    while True:
        if cnt == n: return str(y) + '/' + str(x)
        x, y = moveR(x, y)
        cnt += 1
        
        while x > 1:
            if cnt == n: return str(y) + '/' + str(x)
            x, y = moveDLU(x, y)
            cnt += 1
            
        if cnt == n: return str(y) + '/' + str(x)    
        x, y = moveU(x, y)
        cnt += 1
        
        while y > 1:
            if cnt == n: return str(y) + '/' + str(x)
            x, y = moveDRU(x, y)
            cnt += 1

n = int(input())
print(solution())