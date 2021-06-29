def solution(people, limit):
    answer = 0
    
    people.sort()

    left = 0
    right = len(people) - 1

    while right - left > 0 :
        if people[left] + people[right] <= limit:
            answer += 1
            people[left] = -1
            people[right] = -1
            left += 1
            right -= 1
        else:
            right -= 1
    
    # boat에 태워보내지 못한 사람이 있는지 검사
    for person in people:
        if person != -1:
            answer += 1
    
    return answer