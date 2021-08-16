from collections import deque

def solution(arr):
    answer = [0,0]
    queue = deque([arr])

    while queue:
        s = queue.popleft() # 압축하고자 하는 영역
        num = s[0][0] # 압축하고자 하는 수

        check = True
        for i in s:
            if check == False:
                break
            for j in i:
                if j != num:
                    check = False
                    break
        
        # s 내부에 있는 모든 수가 같은 값일 때
        if check == True:
            answer[num] += 1
        # s를 압축할 수 없을 때
        else:
            length = len(s)//2

            # 4분할 한 정사각형의 원소가 1개일 때
            if length == 1:
                answer[s[0][0]] += 1
                answer[s[0][1]] += 1
                answer[s[1][0]] += 1
                answer[s[1][1]] += 1
            
            # 정사각형을 4분할 해서 queue에 넣음
            else:
                queue.append([s[i][:length] for i in range(length)])
                queue.append([s[i][length:] for i in range(length)])
                queue.append([s[i][:length] for i in range(length, len(s))])
                queue.append([s[i][length:] for i in range(length, len(s))])

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]), [4,9])
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]), [10,15])