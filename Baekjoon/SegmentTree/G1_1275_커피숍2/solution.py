nums, tree = [], []


def build_tree(start, end, node): # 구간 합 트리 생성
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = build_tree(start, mid, node*2) + build_tree(mid+1, end, node*2+1)
    return tree[node]


def get_sum(start, end, node, left, right): # left~right 구간의 합 반환
    if end < left or start > right: return 0
    if start >= left and end <= right: return tree[node]
    mid = (start + end) // 2
    return get_sum(start, mid, node*2, left, right) + get_sum(mid+1, end, node*2+1, left, right)


def change_num(start, end, node, index, diff): # index번째 수를 diff만큼 수정
    if start > index or end < index: return
    tree[node] += diff
    if start == end: return
    mid = (start + end) // 2
    change_num(start, mid, node*2, index, diff)
    change_num(mid+1, end, node*2+1, index, diff)


def main():
    global nums, tree
    n, q = map(int, input().split())
    nums = [0]+list(map(int, input().split())) # 1 2 3 4 5
    tree = [0 for _ in range((n+1)*4)]
    build_tree(0, n, 1)
    for _ in range(q):
        x, y, a, b = map(int, input().split())
        x, y = min(x, y), max(x, y)
        print(get_sum(0, n, 1, x, y))
        diff = b - nums[a]
        nums[a] = b
        change_num(0, n, 1, a, diff)


if __name__ == "__main__":
    main()