answer = []

def hanoi(start, dest, n):
    global answer
    pillars = [1, 0, 0, 0]
    pillars[start] = 1; pillars[dest] = 1
    non_dest = pillars.index(0) # 도착지점이 아닌 곳

    if n == 1: return answer.append([start, dest]) 
    
    hanoi(start, non_dest, n-1) # n-1개의 원판을 도착지점이 아닌 곳에 옮김
    answer.append([start, dest]) # 마지막 원판을 도착지점에 옮김
    hanoi(non_dest, dest, n-1) # n-1개의 원판을 도착지점에 옮김

def solution(n):
    global answer
    hanoi(1, 3, n)
    return answer

print(solution(2),[[1, 2], [1, 3], [2, 3]])