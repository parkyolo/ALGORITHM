import sys
R, C = 0, 0

def binary_search(wrong_spaces, sheets): # 잘못 칠해진 칸의 위치, 사용할 색종이 장수
    wrong_spaces.sort(key=lambda x:x[1])
    
    start, end = max([row[0] for row in wrong_spaces]), max(R, C)+1
    while start < end:
        mid = (start+end) // 2
        cnt = 1
        k = wrong_spaces[0][1] # 열의 최솟값에서 시작
        for r, c in wrong_spaces:
            if c >= k+mid: # 범위를 벗어나면
                cnt += 1 # 색종이 추가
                k = c # 시작 위치 변경
            if cnt > sheets: break
        
        if cnt <= sheets: # 주어진 색종이로 모든 칸을 가릴 수 있으면
            end = mid # 더 작은 범위 탐색
        else: start = mid+1 # 가릴 수 없으면 더 큰 범위 탐색
    
    return end

def main():
    global R, C
    R, C = map(int, input().split()) # 행, 열의 개수
    sheets = int(input()) # 사용할 색종이의 장수
    m = int(input()) # 도화지에 잘못 칠해진 칸의 개수

    wrong_spaces = []
    for _ in range(m):
        wrong_spaces.append(list(map(int, sys.stdin.readline().strip().split())))

    answer = binary_search(wrong_spaces, sheets)
    print(answer)

if __name__ == "__main__":
    main()