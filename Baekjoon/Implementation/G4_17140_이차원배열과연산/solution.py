from collections import Counter

r, c, k = 0, 0, 0
arr = []

def calR(): # R 연산 함수
    max_length = 0  # 가장 큰 행의 길이

    for idx, row in enumerate(arr):
        cnt = Counter(row)                          # 1. 행에 있는 수 : 등장 횟수를 구함

        sub_arr = []
        for e, c in cnt.items():                    # 2. 행,등장 횟수를 sub_arr에 추가
            if e == 0: continue                     # (0은 무시)
            sub_arr.append([e, c])

        sub_arr.sort(key=lambda x:(x[1],x[0]))      # 3. 등장 횟수가 커지는 순으로, 수가 커지는 순으로 정렬
        new_row = sum(sub_arr, [])                  # 4. 정렬한 결과를 수, 등장 횟수의 순으로 하나의 배열에 넣어줌
        max_length = max(max_length, len(new_row))  # 5. 가장 큰 행의 길이를 구함
        arr[idx] = new_row                          # 6. 연산 결과로 행을 갱신
    
    for i in range(len(arr)):                       # 7. 가장 큰 행을 기준으로 0을 채워줌
        while len(arr[i]) < max_length:
            arr[i].append(0)

def row2col(): # 행과 열을 뒤집는 함수
    global arr
    new_arr = []
    for i in range(len(arr[0])):
        sub_arr = []
        for j in range(len(arr)):
            sub_arr.append(arr[j][i])
        new_arr.append(sub_arr)
    arr = new_arr

def calC():
    row2col()   # 1. 행과 열의 뒤집음
    calR()      # 2. R 연산
    row2col()   # 3. 행과 열을 제자리로

def cal(cnt):

    if len(arr) > r and len(arr[0]) > c and arr[r][c] == k: # 배열의 (r, c)에 k가 들어있을 때
        print(cnt) # 최소 시간 출력
        return

    if cnt > 100:   # 100초가 지났을 때
        print(-1)
        return

    if len(arr) >= len(arr[0]): # 행의 개수 >= 열의 개수인 경우
        calR()
    else:                       # 행의 개수 < 열의 개수인 경우
        calC()
    
    cal(cnt+1)

def main():
    global r, c, k, arr
    r, c, k = map(int, input().split())
    r -= 1 # (0, 0)부터 시작하도록 1을 빼줌
    c -= 1
    arr = list(list(map(int, input().split())) for _ in range(3))

    cal(0)

if __name__ == "__main__":
    main()