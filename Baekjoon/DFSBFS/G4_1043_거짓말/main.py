from collections import deque

N, M = map(int, input().split()) # 사람의 수, 파티의 수
know_truth = list(map(int, input().split())) # 진실을 아는 사람의 수, 번호
parties = list(list(map(int, input().split())) for _ in range(M)) # 파티에 오는 사람의 수, 번호

part_in_party = {i:[] for i in range(1, N+1)} # i번 사람이 참여한 파티 번호
people_in_party = {i:[] for i in range(1, M+1)} # i번 파티에 참여하는 사람
for i, party in enumerate(parties):
    party_num = i+1
    people_in_party[party_num] = party[1:]
    for j in range(1, party[0]+1):
        person_num = party[j]
        part_in_party[person_num].append(party_num)

answer = set([i for i in range(1, M+1)])
queue = deque()
know_truth = know_truth[1:]
for i in know_truth:
    queue.append(i)
know_truth = set(know_truth)

while queue:
    p = queue.popleft()
    for party in part_in_party[p]: # 진실을 아는 사람이 참여한 파티를 answer에서 제거
        if party in answer: answer.remove(party)
        for person in people_in_party[party]: # 그 파티에 온 다른 사람을 queue에 추가
            if person not in know_truth:
                queue.append(person)
                know_truth.add(person)

print(len(answer))