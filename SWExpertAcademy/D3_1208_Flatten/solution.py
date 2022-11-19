'''
[S/W 문제해결 기본] 1일차 - Flatten
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

낮은 높이부터 + 1한 값과 높은 높이부터 - 1한 값이 같아지면 작업이 끝나므로
minheap과 maxheap의 root 원소의 차이가 1보다 작아지면 종료한다.
'''

import heapq

T = 10

for test_case in range(1, T+1): 
    n = int(input())
    minheap = list(map(int, input().split()))
    maxheap = [-i for i in minheap]
    heapq.heapify(minheap)
    heapq.heapify(maxheap)

    for i in range(n):
        min_height, max_height = heapq.heappop(minheap), -heapq.heappop(maxheap)
        if max_height - min_height < 2: break
        heapq.heappush(minheap, min_height+1)
        heapq.heappush(maxheap, -(max_height-1))

    min_height, max_height = heapq.heappop(minheap), -heapq.heappop(maxheap)
    print("#%d %d"%(test_case,max_height - min_height))