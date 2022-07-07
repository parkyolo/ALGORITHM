def main():
    N = int(input())
    wires = [list(map(int, input().split())) for _ in range(N)]
    wires.sort()

    cnt = 0
    arr = [b for a, b in wires]
    dp = [1 for _ in range(N)] 
    for i in range(N):
        for j in range(i, -1, -1):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        cnt = max(cnt, dp[i])

    print(N-cnt)

if __name__ == "__main__":
    main()