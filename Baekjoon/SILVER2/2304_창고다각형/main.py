n = int(input())
pillars = [list(map(int, input().split())) for _ in range(n)]

use = [] # 사용되는 기둥을 담을 배열
pillars.sort(key=lambda x:x[0]) # 기둥의 위치로 정렬
front_max = 0 # 앞에 있는 기둥 중 가장 높은 기둥의 높이

for i, pillar in enumerate(pillars):
    check_front = 1 # 앞에 자신보다 높은 기둥이 있는지
    check_back = -1 # 뒤에 자신보다 높은 기둥이 있는지
    if pillar[1] > front_max:
        check_front = -1
        front_max = pillar[1]
    for j in range(i,n):
        if pillars[j][1] > pillar[1]:
            check_back = 1
            break
        if check_front == 1 and check_back == 1: continue # 앞, 뒤로 높은 기둥이 있다면 pass
    use.append(i)

area = 0
for i in range(len(use)-1):
    area += pillars[use[i]][1]
    if pillars[use[i+1]][1] >= pillars[use[i]][1]: # 뒤의 기둥이 더 높을 때
        area += (pillars[use[i+1]][0]-pillars[use[i]][0]-1)*pillars[use[i]][1]
    else: # 뒤의 기둥이 더 낮을 때
        area += (pillars[use[i+1]][0]-pillars[use[i]][0]-1)*pillars[use[i+1]][1]
area += pillars[use[-1]][1]
print(area)