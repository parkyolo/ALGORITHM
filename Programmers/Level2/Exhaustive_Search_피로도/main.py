from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dun = [i for i in range(len(dungeons))]
    # 가능한 모든 경우의 수를 확인
    for seq in permutations(dun, len(dungeons)):
        cur = k
        cnt = 0
        for s in seq:
            if cur >= dungeons[s][0]:
                cnt += 1
                cur -= dungeons[s][1]
            else:
                break
        # 탐험할 수 있는 던전 수가 가장 큰 경우
        answer = max(answer, cnt)
    return answer