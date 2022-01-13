from itertools import permutations

def solution(n, weak, dist):
    dist.sort(key=lambda x:-x) # 이동거리가 긴 순으로 정렬
    for i in range(len(dist)):
        permutation = list(map(list,permutations(dist[:i+1], i+1))) # i명의 순서의 경우의 수
        for p in permutation:
            for j in range(len(weak)):
                friends = p.copy() # 외벽을 고칠 i명의 순서
                circle = weak[j:]+[x+n for x in weak[:j]] # j 지점부터 외벽을 고친다면, j의 앞부분은 n을 더해서 뒤에 붙여줌
                while friends:
                    fix_range = circle.pop(0) + friends.pop(0) # circle[0] + friends[0]만큼 고칠 수 있음
                    while circle and circle[0] <= fix_range: circle.pop(0) # fix_range에 속하는 외벽이라면 pop해줌
                if not circle: return i+1 # 모든 외벽이 고쳐졌다면, return i+1
    return -1 
            


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), 2)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]), 1)