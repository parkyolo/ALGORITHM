from itertools import combinations

def solution(info, query):
    answer = []
    
    # 지원자를 그룹별로 분류
    dic = {}
    for i in info:
        app = i.split()
        key = app[:-1]
        value = int(app[-1])
        for j in range(5):
            combi = combinations(range(4), j)
            for c in combi:
                key_copy = key.copy()
                for k in c:
                    key_copy[k] = '-'
                new_key = ''.join(key_copy)
                if new_key in dic:
                    dic[new_key].append(value)
                else:
                    dic[new_key] = [value]
    
    for value in dic.values():
        value.sort()
    
    # 오름차순으로 정렬된 배열에서 binary search
    for q in query:
        con = [i for i in q.split() if i != "and"]
        new_con = "".join(con[:-1])
        score = int(con[-1])
        if new_con in dic:
            value = dic[new_con]
            start = 0
            end = len(value)
            while start != end and start != len(value):
                mid = (start + end) // 2
                if value[mid] >= score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(value)-start)
        else:
            answer.append(0)
    return answer

answer = solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
print(answer)