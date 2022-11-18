'''
[S/W 문제해결ㄹ 기본] 1일차 - View
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
'''

T = 10

for test_case in range(1, T + 1):
    
    n = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    for i in range(2, n-2):
        # 현재 높이가 (왼쪽과 오른쪽 2개의 높이 중 가장 높은 곳)보다 높으면, 차를 answer에 더해준다.
        answer += max(0, heights[i] - max(heights[i-2], heights[i-1], heights[i+1], heights[i+2]))
    
    print("#%d %d"%(test_case, answer))