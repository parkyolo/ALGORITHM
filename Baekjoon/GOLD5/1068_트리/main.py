from collections import deque
n = int(input())
nodes = list(map(int, input().split()))
m = int(input()) # 지울 노드

tree = [[] for _ in range(n)]
root = -1 # 루트 노드
for child, parent in enumerate(nodes):
    if parent == -1: root = child
    else:
        tree[parent].append(child)

if root == m: print(0); exit(); # 루트 노드를 지우면 리프 노드는 0개

# m과 m의 자식 노드들을 삭제
m_parent = nodes[m]
tree[m_parent].remove(m)
queue = deque([m])
while queue:
    delete_node = queue.popleft()
    if tree[m]:
        for node in tree[m]:
            queue.append(node)
        tree[m] = []

# 리프 노드의 개수 구하기
answer = 0
queue = deque([root])
while queue:
    parent = queue.popleft()
    if tree[parent]:
        for child in tree[parent]:
            queue.append(child)
    else: # 자식 노드가 없을 경우
        answer += 1
print(answer)