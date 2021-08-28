def solution(s):
    answer = " ".join(map(lambda s:s[0].upper()+s[1:].lower() if s else s, s.split(" ")))
    
    # 연속된 공백을 처리할 수 없음
    # answer = " ".join(i[0].upper()+i[1:].lower() for i in s.split(" "))
    return answer

print(solution("3people unFollowed me"),"3people Unfollowed Me")
print(solution("for the last week"),"For The Last Week")