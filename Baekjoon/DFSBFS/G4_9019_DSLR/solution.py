from collections import deque
import sys
input = sys.stdin.readline


def calD(n):
    return (2*n)%10000


def calS(n):
    return (n+10000-1)%10000


def calL(n):
    return (n%1000)*10+(n//1000)


def calR(n):
    return (n%10)*1000+(n//10)


def bfs(a, b):
    queue = deque()
    queue.append((a, ""))
    v = [False for _ in range(10000)]   # 0부터 9999까지 등장한 숫자는 True
    v[a] = True

    while queue:
        reg, res = queue.popleft()  # 레지스터 값, 연산 과정
        if reg == b:
            print(res)
            return
        
        d, s, l, r = calD(reg), calS(reg), calL(reg), calR(reg) # 연산한 값
        if not v[d]:
            queue.append((d, res+"D"))
            v[d] = True
        if not v[s]:
            queue.append((s, res+"S"))
            v[s] = True
        if not v[l]:
            queue.append((l, res+"L"))
            v[l] = True
        if not v[r]:
            queue.append((r, res+"R"))
            v[r] = True
        

def solution():
    A, B = map(int, input().split())
    bfs(A, B)
    

T = int(input())
for _ in range(T):
    solution()