def rev(x, y, mat):
    dx = [-1 ,-1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for d in range(9):
        if mat[x+dx[d]][y+dy[d]] == '0': mat[x+dx[d]][y+dy[d]] = '1'
        else: mat[x+dx[d]][y+dy[d]] = '0'
    return mat

n, m = map(int, input().strip().split())

matrixA = []
matrixB = []
for _ in range(n):
    matrixA.append((list(input())))
for _ in range(n):
    matrixB.append((list(input())))

if matrixA == matrixB: # 처음부터 같은 matrix가 들어왔을 경우
    print(0)
elif n < 3 or m < 3: # n이나 m이 3보다 작을 경우
    print(-1)
    exit()

cnt = 0
# 가장 바깥쪽 행과 열을 제외하고 탐색
for i in range(1, n-1):
    for j in range(1, m-1):
        # 3x3 행렬에서 가장 첫 번째 원소가 서로 다를 때
        if matrixA[i-1][j-1] != matrixB[i-1][j-1]:
            # 부분 행렬의 모든 원소를 뒤집어줌
            matrixA = rev(i, j, matrixA)
            cnt += 1
            
if matrixA == matrixB:
    print(cnt)
else:
    print(-1)