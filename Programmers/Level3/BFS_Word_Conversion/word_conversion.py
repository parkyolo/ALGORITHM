from collections import deque

def solution(begin, target, words):
    answer = 0
    
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        # word : 현재 단어, count : 현재 단계
        word, count = queue.popleft()

        # begin을 target으로 변환했으면 count를 return
        if word == target:
            return count
        # 변환할 수 없는 경우 0을 return
        elif count == len(words):
            return 0

        for i in words:
            diff = 0 
            # --> 기존 코드
            # for j in range(len(word)):
            #     if i[j] == word[j]:
            #         cnt += 1
            # if cnt == len(word)-1:
            #     queue.append([i, count+1])

            # --> 수정한 코드
            # word와 i의 다른 알파벳 count
            diff = sum([x != y for x, y in zip(word, i)])
            # word와 i가 한 개의 알파벳만 다를 때 queue에 넣음
            if diff == 1:
                queue.append([i, count+1])

    # begin을 target으로 변환할 수 없는 경우 0을 return
    return 0

answer = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(answer)