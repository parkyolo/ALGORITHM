import sys
INF = sys.maxsize

n = int(input())    # 식재료의 개수
mp, mf, ms, mv = map(int, input().split())  # 단백질, 지방, 탄수화물, 비타민의 최소 영양성분
nutrients = [list(map(int, input().split())) for _ in range(n)] # 식재료의 영양성분

combi = []
min_cost = INF
min_combi = []


def getSum():
    global min_cost, min_combi
    
    pi, fi, si, vi, ci = 0, 0, 0, 0, 0
    for idx in combi:
        pi += nutrients[idx][0]
        fi += nutrients[idx][1]
        si += nutrients[idx][2]
        vi += nutrients[idx][3]
        ci += nutrients[idx][4]
    
    if pi >= mp and fi >= mf and si >= ms and vi >= mv:
        if ci < min_cost:
            min_cost = ci
            min_combi = [i for i in combi]
                
        
def getCombi(k):
    getSum()
    
    for i in range(k, n):
        if i not in combi:
            combi.append(i)
            getCombi(i+1)
            combi.pop()
            
    
getCombi(0)
    

if min_cost == INF: print(-1)
else:
    print(min_cost)
    print(' '.join([str(i+1) for i in min_combi]))