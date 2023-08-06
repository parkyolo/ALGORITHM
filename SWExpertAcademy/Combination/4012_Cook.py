'''
4012. [모의 SW 역량테스트] 요리사
(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&categoryId=AWIeUtVakTMDFAVH&categoryType=CODE&problemTitle=4012&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

재귀로 조합 구현
'''

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    synergy = list(list(map(int, input().strip().split())) for _ in range(N))

    def cal(arr): # 시너지 계산
        global synergy
        res = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                res += synergy[arr[i]][arr[j]]
                res += synergy[arr[j]][arr[i]]
        return res

    def comb(idx, n): # a의 조합 구하기
        global arr, a_arr

        if n == N//2:
            a = [i for i in range(N) if arr[i]]
            return a_arr.append(a)

        for i in range(idx, N):
            if arr[i]: continue
            arr[i] = 1
            comb(i, n+1)
            arr[i] = 0

    arr = [0 for _ in range(N)]
    a_arr = []
    comb(0, 0)

    min_diff = 2147483648
    for a in a_arr: # 시너지 차이의 최솟값 구하기
        b = [i for i in range(N) if i not in a]
        a_synergy = cal(a)
        b_synergy = cal(b)
        diff = max(a_synergy, b_synergy) - min(a_synergy, b_synergy)
        min_diff = min(min_diff, diff)

    print('#'+str(test_case)+' '+str(min_diff))