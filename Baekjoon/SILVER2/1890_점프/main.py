n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
v = [[0 for _ in range(n)] for _ in range(n)]

v[0][0] = 1
for i in range(n):
    for j in range(n):
        if game[i][j] == 0: break
        if v[i][j] > 0:
            if i + game[i][j] < n:
                v[i+game[i][j]][j] += v[i][j]
            if j + game[i][j] < n:
                v[i][j+game[i][j]] += v[i][j]
print(v[-1][-1])