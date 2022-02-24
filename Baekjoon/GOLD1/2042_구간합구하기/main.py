nums = []
tree = []

def segment_tree(start, end, node): # 세그먼트 트리 생성
    if start == end: tree[node] = nums[start]
    else:
        mid = (start+end)//2
        tree[node] = segment_tree(start, mid, node*2) + segment_tree(mid+1, end, node*2+1)
    return tree[node]

def _sum(start, end, node, left, right): # 구간 합 구하기
    if left > end or right < start: return 0
    elif left <= start and right >= end: return tree[node]
    mid = (start+end)//2
    return _sum(start, mid, node*2, left, right) + _sum(mid+1, end, node*2+1, left, right)

def update(start, end, node, index, diff): # 값 변경
    if index < start or index > end: return
    tree[node] += diff
    if start == end: return
    mid = (start+end)//2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

if __name__=="__main__":
    n, m, k = map(int, input().split())
    for _ in range(n):
        nums.append(int(input()))
    tree = [0 for _ in range(n*4)]
    segment_tree(0, n-1, 1)
    # print(tree)
    for _ in range(m+k):
        a, b, c = map(int, input().split())
        if a == 1:
            diff = c - nums[b-1]
            nums[b-1] = c
            update(0, n-1, 1, b-1, diff)
            # print(tree)
        else:
            print(_sum(0, n-1, 1, b-1, c-1))