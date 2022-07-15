N, L, R, X = 0, 0, 0, 0
A = []
cnt = 0

def is_okay(problems):
    """
    1. 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다.
    2. 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.
    """
    if (L <= sum(problems) <= R) and (max(problems)- min(problems) >= X):
        return True
    else:
        return False

def comb(k, problems, n): # 문제 조합 구하기
    global cnt
    if len(problems) == n:
        if is_okay(problems):
            cnt += 1 # 조건에 맞으면 방법의 수 += 1
    
    for i in range(k, N): # 조합 구하기
        problems.append(A[i])
        comb(i+1, problems, n)
        problems.pop()

def main():
    global N, L, R, X, A
    N, L, R, X = map(int, input().split())
    A = list(map(int, input().split())) # 난이도
    for n in range(2, N+1):
        """
        2개 이상의 문제에 대해 조합을 구하고, 조건에 맞는지 검사
        """
        comb(0, [], n)

    print(cnt) # 방법의 수 출력

if __name__ == "__main__":
    main()