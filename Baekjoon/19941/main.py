n, k = map(int, input().split())
ham = [0 for _ in range(n)]
per = [0 for _ in range(n)]
s = input()
for index, i in enumerate(s):
    if i == "H": ham[index] = 1
    elif i == "P": per[index] = 1
cnt = 0
for pidx in range(n):
    if per[pidx] == 1: # 사람이 있을 때
        eat = False # 먹었는지 확인
        for hidx in range(pidx-k, pidx):
            if hidx >= 0:
                if ham[hidx] == 1: # k 거리 안에 햄버거가 있을 경우
                    ham[hidx] = -1
                    cnt += 1
                    eat = True
                    break
        if eat == False: # 사람 앞에 햄버거가 없을 경우 뒤도 확인
            for hidx in range(pidx+1, pidx+k+1):
                if hidx < n:
                    if ham[hidx] == 1: # k 거리 안에 햄버거가 있을 경우
                        ham[hidx] = -1
                        cnt += 1
                        break
print(cnt)