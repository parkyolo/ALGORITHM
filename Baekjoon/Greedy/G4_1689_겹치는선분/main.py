import sys, heapq

def main():
    N = int(input())
    lines = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    lines.sort()

    heap = [] # 겹치는 선분
    answer = 0
    for s, e in lines:
        while len(heap) and heap[0] <= s: # 끝나는 좌표가 가장 작은 선분이 현재 선분과 겹치지 않을 때
            heapq.heappop(heap) # heap에서 제거
        heapq.heappush(heap, e) # 겹치는 선분 추가
        answer = max(answer, len(heap))

    print(answer)

if __name__ == "__main__":
    main()