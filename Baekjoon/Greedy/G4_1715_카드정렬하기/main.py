import heapq
import sys

def main():
    N = int(input())
    heap = []
    for _ in range(N):
        heapq.heappush(heap, int(sys.stdin.readline().strip()))
        
    if N == 1: # N == 1이면 비교할 필요 없음
        print(0)
        return
        
    ans = 0
    while len(heap) > 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap) 
        ans += a+b # 비교 횟수가 작은 것끼리 묶음
        heapq.heappush(heap, a+b) # 합친 카드를 다시 큐에 추가

    ans += heap[0] + heap[1]
    print(ans)
    return

if __name__ == "__main__":
    main()