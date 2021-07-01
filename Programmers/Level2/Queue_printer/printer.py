def solution(priorities, location):
    answer = 0
    
    # 대기목록에 문서가 1개일 때 바로 1을 리턴
    if len(priorities) == 1:
        return 1    
    
    # 문서의 처음 위치를 저장
    locations = []
    for i in range(len(priorities)):
        locations.append(i)
        
    check = True # 인쇄가 끝났는지 확인
    idx = 0 # 현재 문서의 J의 index
    while check:
        now = priorities[idx] # 현재 문서의 J의 중요도
        print_ = True # 현재 문서 J를 인쇄할 것인지 확인
        for i in range(idx+1, len(priorities)):
            # 나머지 인쇄 대기목록의 문서가 J보다 중요도가 높으면 J를 대기목록의 마지막에 넣음
            if priorities[i] > now: 
                priorities.pop(idx)
                priorities.append(now)
                loc = locations.pop(idx)
                locations.append(loc)
                print_ = False # J를 프린트하지 않음
                break
        
        # J를 인쇄했으면 다음 idx의 문서부터 검사
        if print_:
            idx += 1
        
        # 모든 문서의 중요도가 인쇄되었는지 검사
        printed = 0
        for i in range(len(priorities)-1):
            if priorities[i] >= priorities[i+1]:
                printed += 1   
        if printed == len(priorities)-1:
            check = False
    
    # location에 해당하는 문서가 인쇄된 index를 반환
    for i in range(len(locations)):
        if locations[i] == location:
            answer = i+1
            
    return answer

answer = solution([2, 1, 3, 2], 2)
print(answer) #1