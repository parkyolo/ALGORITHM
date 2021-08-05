def solution(n, words):
    visited = []

    visited.append(words[0])
    for i in range(1,len(words)):
        word = words[i]
        # 끝말잇기가 이어지는지 확인
        if words[i-1][-1] != word[0]:
            return [i%n+1, i//n+1]
        # 이미 등장했던 단어인지 확인
        elif word in visited:
            return [i%n+1, i//n+1]
        visited.append(word)

    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]),[3,3])
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]),[0,0])
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]),[1,3])