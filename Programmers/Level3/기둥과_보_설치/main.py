def impossible(structures):
    for x, y, a in structures:
        if a == 0: # 기둥
            if y != 0 and (x-1, y, 1) not in structures and (x, y, 1) not in structures and (x, y-1, 0) not in structures:
                return True
        else: # 보
            if (x, y-1, 0) not in structures and (x+1, y-1, 0) not in structures and not ((x-1, y, 1) in structures and (x+1, y, 1) in structures):
                return True
    return False

def solution(n, build_frame):
    structures = set()

    for x, y, a, b in build_frame:
        if b == 1: # 구조물을 설치
            structures.add((x, y, a))
            if impossible(structures): structures.remove((x, y, a))
        else: # 구조물을 제거
            structures.remove((x, y, a))
            if impossible(structures): structures.add((x, y, a))
    
    answer = list(map(list, structures))
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer

# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
# print([[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
print([[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])