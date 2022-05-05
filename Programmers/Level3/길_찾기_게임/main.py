import sys
sys.setrecursionlimit(10**6)

def tree(root, nodes, tree_): # 트리 생성
    left, right = [], []
    for node in nodes: # 루트 노드의 왼쪽 노드, 오른쪽 노드를 나눠줌
        if node[0] < root[0]: left.append(node)
        elif node[0] > root[0]: right.append(node)
    
    left_root, right_root = [0, 0, 0], [0, 0, 0]
    if left: # 왼쪽 노드가 있을 때
        left_root = max(left, key=lambda x:x[1])
        tree_[left_root[2]] = tree(left_root, left, tree_)
    if right: # 오른쪽 노드가 있을 때
        right_root = max(right, key=lambda x:x[1])
        tree_[right_root[2]] = tree(right_root, right, tree_)
        
    return [left_root[2], right_root[2]]

def traversal(tree_, node, team1, team2): # 트리 순회
    team1.append(node) # 전위 순회

    if tree_[node][0] > 0:
        traversal(tree_, tree_[node][0], team1, team2)
    if tree_[node][1] > 0:
        traversal(tree_, tree_[node][1], team1, team2)

    team2.append(node) # 후위 순회

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    # 트리 생성
    # tree[i] : i가 부모 노드일 때 [왼쪽 자식 노드, 오른쪽 자식 노드] (0이면 자식 노드가 없다)
    root = max(nodeinfo, key=lambda x:x[1])
    tree_ = [[] for _ in range(len(nodeinfo)+1)]
    tree_[root[2]] = tree(root, nodeinfo, tree_)
    
    # 순회
    # team1 : 전위 순회, team2 : 후위 순회
    team1, team2 = [], []
    traversal(tree_, root[2], team1, team2)

    return [team1, team2]

print(solution(	[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]), 	[[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])