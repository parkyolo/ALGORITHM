T = int(input()) # 테스트 케이스의 개수

n = [] # 동전의 가지 수
m = [] # 만들어야 할 금액
coins = [] # 동전의 각 금액

for t in range(T):
    n.append(int(input()))
    coins.append(list(map(int, input().split())))
    m.append(int(input()))

for t in range(T):
    price = m[t] #100
    coin = coins[t] #[1,2]
    cnt = [0 for _ in range(price+1)]
    cnt[0] = 1

    for i in range(n[t]):
        for j in range(1, price+1):
            if j-coin[i] >= 0:
                # cnt[j]에 cnt[j-coin[i]]를 더한다.
                cnt[j] += cnt[j-coin[i]]

    print(cnt[price])