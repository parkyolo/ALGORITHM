import re
from collections import deque

def solution(user_id, banned_id):
    answer = 0

    off_id_dict = {id.replace("*", "."):[] for id in banned_id} # {불량 사용자 : [제재 아이디1, 제재 아이디2, ...], ...}
    # 1. user id 중 불량 사용자 id와 매핑되는 응모자 아이디를 off_id_dict[b_id]에 추가
    for u_id in user_id: # u_id : 사용자 id
        for b_id in off_id_dict.keys(): # b_id : 불량 사용자 id
            if re.compile(b_id).match(u_id) and len(b_id) == len(u_id): off_id_dict[b_id].append(u_id)
    
    # 2. 각 불량 사용자의 제재 아이디 목록을 queue에 담음
    queue = deque()
    for o_id in off_id_dict[banned_id[0].replace("*", ".")]: # 첫 번째 불량 사용자의 제재 아이디 목록을 queue에 담음
        queue.append([set([o_id]), 1])

    result = []
    while queue:
        id_set, idx = queue.popleft()
        if idx == len(banned_id): # 모든 불량 사용자의 제재 아이디가 하나씩 담겼을 때
            if id_set not in result: # 중복되지 않는 제재 아이디 목록을 result에 추가
                result.append(id_set)
            continue
        for o_id in off_id_dict[banned_id[idx].replace("*", ".")]:
            if o_id in id_set: continue # 제재 아이디가 중복되는 경우 continue
            queue.append([id_set|set([o_id]), idx+1])

    answer = len(result)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]), 2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]), 2)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]), 3)