from collections import deque

N = 0
tree = []

def bfs(startNode, exceptNode=0):
    visited = [0 for _ in range(N+1)]
    visited[startNode] = 1
    visited[exceptNode] = 1

    queue = deque()
    queue.append([startNode, 0])

    farNode = [0, 0]
    while queue:
        curNode, dist = queue.popleft()

        if farNode[1] < dist:
            farNode = [curNode, dist]

        for nextNode, nextEdge in tree[curNode]:
            if visited[nextNode]: continue
            visited[nextNode] = 1
            queue.append([nextNode, dist+nextEdge])

    return farNode

def input_():
    global N, tree
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        node1, node2, weight = map(int, input().split())
        tree[node1].append([node2, weight])
        tree[node2].append([node1, weight])

def main():
    input_()

    a = bfs(1)[0]
    b = bfs(a)[0]

    print(max(bfs(a, b)[1], bfs(b, a)[1]))

if __name__ == "__main__":
    main()