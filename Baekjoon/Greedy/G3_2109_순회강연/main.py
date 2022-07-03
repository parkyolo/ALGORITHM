import heapq

def main():
    n = int(input())
    pd = list(list(map(int, input().split())) for _ in range(n))
    pd.sort(key=lambda x:x[1]) # d가 작은 순으로 정렬

    heap = [] # 할 수 있는 강연 리스트
    for p, d in pd:
        heapq.heappush(heap, p)
        if len(heap) > d: # d일 안에 모든 강연을 하지 못하면
            heapq.heappop(heap) # 강연료가 가장 작은 것 제거

    print(sum(heap))

if __name__ == "__main__":
    main()