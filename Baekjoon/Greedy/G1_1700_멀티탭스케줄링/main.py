n, k = map(int, input().split())
apps = list(map(int, input().split()))
unplug_cnt = 0
multitap = []
for idx, app in enumerate(apps):
    if app in multitap: continue # 멀티탭에 이미 기기가 꽂혀있을 때
    elif len(multitap) < n: multitap.append(app) # 멀티탭에 자리가 남아있을 때
    else: # 플러그를 뽑아야할 때
        dist = [] # 멀티탭에 꽂힌 기기들이 다시 등장할 거리
        check = False
        for tap in multitap:
            if check == True: break
            try: # 기기가 다시 등장한다면
                dist.append(apps[idx:].index(tap))
            except: # 다시 등장하지 않는다면
                dist.append(101)
                check = True
        
        if check:
            multitap[dist.index(101)] = app
        else:
            multitap[dist.index(max(dist))] = app
        unplug_cnt += 1 # 횟수 count
        
print(unplug_cnt)