from collections import deque
board = [list(map(int, input().split())) for _ in range(5)]
nums = set()
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(5):
    for j in range(5):
        queue.append([i, j, str(board[i][j])])
while queue:
    x, y, num = queue.popleft()
    if len(num) == 6:
        if num not in nums: nums.add(num)
        continue
    for i in range(4):
        if 0 <= x+dx[i] < 5 and 0 <= y+dy[i] < 5:
            queue.append([x+dx[i], y+dy[i], num+str(board[x+dx[i]][y+dy[i]])])
# print(nums)
print(len(nums))