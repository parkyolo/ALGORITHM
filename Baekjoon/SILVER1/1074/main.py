def recur(n, i, j):
    global cnt
    if n == 1:
        if i == r and j == c:
            print(cnt)
            exit(0)
        cnt += 1
        return
    # r,c 가 4분할 안에 없을 경우 4분할 크기만큼 cnt 에 더해줌
    if not (i <= r < i + n and j <= c < j + n):
        cnt += n*n
        return
    n //= 2
    # 사각형을 4분할
    recur(n, i, j)
    recur(n, i, j+n)
    recur(n, i+n, j)
    recur(n, i+n, j+n)

n, r, c = map(int, input().split())
cnt = 0
recur(2**n, 0, 0)