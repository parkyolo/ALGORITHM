def solution(price, money, count):
    total = 0 # 놀이기구의 총 이용료
    for i in range(1, count+1):
        total += price*i
    
    if total > money:
        return total - money
    else:
        return 0
    
    # return abs(min(money - sum([i*price for i in range(1, count+1)]),0))

print(solution(3,20,4),10)