N, M = map(int, input().split())
nums = list(int(input()) for _ in range(N))
MAX = max(nums)

tree = [0 for _ in range(4*N)]

def init(start, end, node): 
    if start == end:
        tree[node] = (nums[start], nums[start])
        return tree[node]
    mid = (start + end) // 2
    left = init(start, mid, node*2)
    right = init(mid+1, end, node*2+1)
    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]

def get_val(start, end, node, left, right):
    if left > end or right < start: return (MAX, 0)
    if left <= start and end <= right: return tree[node]
    mid = (start + end) // 2
    left_ = get_val(start, mid, node*2, left, right)
    right_ = get_val(mid+1, end, node*2+1, left, right)
    return (min(left_[0], right_[0]), max(left_[1], right_[1]))

init(0, N-1, 1) # 트리 생성
for _ in range(M):
    a, b = map(int, input().split())
    ans = get_val(0, N-1, 1, a-1, b-1) # 구간의 최솟값, 최댓값 구하기
    print(ans[0], ans[1])