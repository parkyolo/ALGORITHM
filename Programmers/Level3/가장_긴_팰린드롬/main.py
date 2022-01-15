def solution(s):
    n = len(s)
    reversed_s = ''.join(reversed(list(s))) # s를 뒤집은 문자열
    # 길이가 n-i (0~n)인 부분문자열
    # s[j:n-i+j]를 뒤집었을 때의 위치인, reversed_s[i-j:n-j]를 비교
    for i in range(n):
        for j in range(i+1):
            if s[j:n-i+j] == reversed_s[i-j:n-j]:
                return n-i

print(solution("abcdcba"), 7)
print(solution("abacde"), 3)