n = int(input())
vertices = []
for _ in range(n):
    vertices.append(list(map(int, input().split())))

vertices.reverse()
vertices.append(vertices[0])
result = 0
for i in range(n):
    result += vertices[i][0]*vertices[i+1][1]
    result -= vertices[i][1]*vertices[i+1][0]

result //= 2
print(abs(result))