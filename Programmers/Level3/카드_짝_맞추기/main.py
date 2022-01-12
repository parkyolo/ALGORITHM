from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy
import sys

def move(board, start, dest):
    if start == dest: return 0
    queue = deque([(start[0], start[1], 0)])
    v = set([start])
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy # move
            cx, cy = x, y # ctrl + move
            while True:
                if 0 <= cx+dx < 4 and 0 <= cy+dy < 4:
                    cx, cy = cx+dx, cy+dy
                    if board[cx][cy] != 0: break
                else: break
            
            if (nx, ny) == dest or (cx, cy) == dest: # 카드에 도착
                return cnt + 1
            
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in v:
                queue.append((nx, ny, cnt+1))
                v.add((nx, ny))
            if (cx, cy) not in v:
                queue.append((cx, cy, cnt+1))
                v.add((cx, cy))

def get_cnt(board, cards, curr, order, move_cnt):
    if len(order) == 0: return move_cnt # 모든 카드를 확인했을 때 조작 횟수 반환
    idx = order[0] # 뒤집을 카드
    new_board = deepcopy(board)

    # start1 : 첫 번째 카드부터 뒤집었을 때의 조작 횟수
    # start2 : 두 번째 카드부터 뒤집었을 때의 조작 횟수
    start1 = move(board, curr, cards[idx][0]) + move(board, cards[idx][0], cards[idx][1]) + 2
    start2 = move(board, curr, cards[idx][1]) + move(board, cards[idx][1], cards[idx][0]) + 2

    # 뒤집은 카드 표시
    new_board[cards[idx][0][0]][cards[idx][0][1]] = 0
    new_board[cards[idx][1][0]][cards[idx][1][1]] = 0

    if start1 < start2: return get_cnt(new_board, cards, cards[idx][1], order[1:], move_cnt+start1)
    else: return get_cnt(new_board, cards, cards[idx][0], order[1:], move_cnt+start2)

def solution(board, r, c):
    answer = sys.maxsize

    cards = defaultdict(list) # 카드 번호 : [위치1, 위치2]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))

    for permu in permutations(cards.keys(), len(cards)):
        cnt = get_cnt(board, cards, (r, c), permu, 0)
        if cnt < answer: answer = cnt

    return answer

print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
print(solution(	[[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)