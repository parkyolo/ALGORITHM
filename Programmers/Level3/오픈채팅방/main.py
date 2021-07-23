def solution(record):
    answer = []
    msg = {}

    # 마지막으로 변경된 닉네임을 msg에 저장
    for r in record:
        rec = r.split()
        if rec[0] == "Leave":
            continue
        uid = rec[1]
        nickname = rec[2]
        msg[uid] = nickname

    # msg에 저장된 [마지막으로 변경된] 닉네임으로 채팅방 출력 메시지를 answer에 저장
    for r in record:
        rec = r.split()
        act = rec[0]
        uid = rec[1]
        if act == "Enter":
            answer.append(msg[uid]+"님이 들어왔습니다.")
        elif act == "Leave":
            answer.append(msg[uid]+"님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))