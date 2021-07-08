n = int(input())
price = list(map(int, input().split()))

# 카드 _개를 갖기 위해 지불해야하는 금액의 최댓값을 저장하는 배열
r = [0 for _ in range(n)]
for j in range(n):
    q = price[j]
    # 카드 j개를 갖기 위해 지불해야 하는 금액의 최댓값을 구함
    for i in range(j):
        q = max(q, price[i]+ r[j-i-1])
    # j번째 index에 카드 j를 갖기 위해 지불해야 하는 금액의 최댓값이 저장됨
    r[j] = q

answer = r[n-1]
print(answer)