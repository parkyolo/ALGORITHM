import sys

N, M = map(int, input().split())
nums = list(int(input()) for _ in range(N))
tree = [0 for _ in range(4*N)]
MAX  = max(nums)

def sort_(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(sort_(start, mid, node*2), sort_(mid+1, end, node*2+1))
    return tree[node]

def find(start, end, node, left, right):
    if left > end or right < start: return MAX
    if left <= start and right >= end: return tree[node]
    mid = (start + end) // 2
    return min(find(start, mid, node*2, left, right), find(mid+1, end, node*2+1, left, right))

sort_(0, N-1, 1)

# print(tree)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(find(0, N-1, 1, a-1, b-1))
