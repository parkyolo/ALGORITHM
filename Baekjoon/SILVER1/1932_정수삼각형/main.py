length = int(input())

triangle = []
for i in range(length):
    triangle.append(list(map(int, input().split())))

for i in range(1, length):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

answer = max(triangle[length-1])
print(answer)