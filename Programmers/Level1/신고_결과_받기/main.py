def solution(id_list, report, k):
    answer = []
    reported_cnt = {uid:0 for uid in id_list} # key가 신고된 횟수
    reported_user = {uid:[] for uid in id_list} # key가 신고한 user
    for r in report:
        uid, ru = r.split(" ") # 신고한 user, 신고당한 user
        if ru not in reported_user[uid]: # 한 유저가 같은 유저를 여러 번 신고한 경우를 제외
            reported_cnt[ru] += 1
            reported_user[uid].append(ru)

    # print(reported_cnt)
    # print(reported_user)
    
    for uid in id_list:
        cnt = 0
        ru = reported_user[uid]
        for i in ru:
            if reported_cnt[i] >= k: cnt += 1
        answer.append(cnt)
    return answer