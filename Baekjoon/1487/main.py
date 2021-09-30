n = int(input())
buyer = []
for i in range(n):
    buyer.append(list(map(int, input().split())))
buyer.sort(key=lambda x:x[0])
price = 0 # 이익을 최대로 하는 가격
max_profit = 0 # 최대 이익
for i in range(n):
    profit = 0 # 이익
    for j in range(i,n):
        if buyer[i][0] - buyer[j][1] > 0: # 이익을 낼 수 있을때만 판매
            profit += buyer[i][0] - buyer[j][1] # 이익은 판매 가격에서 배송비를 뺀 값
    if profit > max_profit:
        price = buyer[i][0]
        max_profit = profit
print(price)