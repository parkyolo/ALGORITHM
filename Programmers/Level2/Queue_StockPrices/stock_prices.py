def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        price = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                price = j - i
                break
        if price == 0:
            price = len(prices) - i - 1
        answer.append(price)
        
    return answer

answer = solution([1, 2, 3, 2, 3])
print(answer)