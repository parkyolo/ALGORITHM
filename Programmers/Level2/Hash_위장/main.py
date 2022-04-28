def solution(clothes):
    answer = 1
    closet = dict()
    for cloth, category in clothes: # 카테고리별로 count
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
            
    for category, cloth in closet.items():
        answer *= cloth+1 # 해당 카테고리를 안입는 경우까지 더해서 곱해줌
        
    return answer-1 # 아무것도 안입는 경우를 빼줌

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]), 5)
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]), 3)
print(solution([["round_glasses", "eyewear"], ["black_sunglasses", "eyewear"], ["blue_t_shirt", "tops"], ["jeans", "bottoms"], ["long_coat", "outerwear"]]), 23)