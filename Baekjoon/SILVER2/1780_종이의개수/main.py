n = int(input())
paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

cnt_1 = 0
cnt0 = 0
cnt1 = 0

def divide_and_conquer(x, y, m):
    global cnt_1, cnt0, cnt1
    curr = paper[x][y]

    for i in range(x, x+m):
        for j in range(y, y+m):
            if paper[i][j] != curr: # 종이가 모두 같은 수가 아니라면
                for k in range(3):
                    for l in range(3):
                        divide_and_conquer(x+k*(m//3), y+l*(m//3), m//3)
                return
    
    if curr == -1: cnt_1 += 1
    elif curr == 0: cnt0 += 1
    else: cnt1 += 1
    return

divide_and_conquer(0, 0, n)

print(cnt_1)
print(cnt0)
print(cnt1)

# queue = deque()
# queue.append([0, 0, n]) # 시작 x, y, 길이 m

# while queue:
#     x, y, m = queue.popleft()
#     sub_matrix = [row[y:y+m] for row in paper[x:x+m]]
#     if sum([row.count(-1) for row in sub_matrix]) == m*m:
#         cnt_1 += 1
#     elif sum([row.count(0) for row in sub_matrix]) == m*m:
#         cnt0 += 1
#     elif sum([row.count(1) for row in sub_matrix]) == m*m:
#         cnt1 += 1
#     else:
#         for i in range(3):
#             for j in range(3):
#                 queue.append([x+i*m//3, y+j*m//3, m//3])