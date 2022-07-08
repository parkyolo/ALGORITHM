def main():
    N, M = map(int, input().split())
    classes = list(map(int, input().split()))

    start, end = max(classes), sum(classes)+1 # 블루레이의 크기는 강의 하나의 크기 이상이어야 함
    while start < end:
        mid = (start+end)//2 # 블루레이 크기
        cnt = 1 # 블루레이 개수
        temp = mid
        for class_ in classes: # 필요한 블루레이 개수 count
            if class_ > temp:
                temp = mid - class_
                cnt += 1
            else:
                temp -= class_
        
        if cnt <= M: # M개 이하일 때 더 작은 범위 탐색
            end = mid
        else:
            start = mid+1
    
    print(end)

if __name__ == "__main__":
    main()