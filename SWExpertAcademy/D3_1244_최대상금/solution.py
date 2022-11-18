'''
[S/W 문제해결 응용] 2일차 - 최대 상금
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
'''

def change(board, time): # 숫자판의 위치를 바꾸는 함수
    global answer
    if answer == max_value:         # 이미 최대 숫자를 만들었다면 return
        return
    
    if (board, time) in visited:    # 이미 방문한 board와 time이라면 return
        return

    visited.add((board, time))

    if time == n:                   # 모든 횟수를 교환했다면 answer 갱신
        answer = max(answer, int(board))
        return
    
    for i in range(len(board)):     # 모든 조합으로 숫자판을 교환
        for j in range(i+1,len(board)):
            new_board = board[:i] + board[j] + board[i+1:j] + board[i] + board[j+1:]
            change(new_board, time+1)

T = int(input())

for test_case in range(1, T + 1):
    board, n = input().split()
    n =  int(n)
    
    visited = set() # 방문 체크
    answer = 0      # 정답

    max_value = ''.join(str(i) for i in sorted(list(map(int, list(board))), reverse=True))  # 숫자판으로 만들 수 있는 가장 큰 수

    change(board, 0)
    print("#%d %d"%(test_case, answer))