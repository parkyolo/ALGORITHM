def dp(sticker):

    if len(sticker) < 3:
        return max(sticker)

    sticker[-2] = max(sticker[-1], sticker[-2])
    for i in range(len(sticker)-3, -1, -1):
        sticker[i] = max(sticker[i+1], sticker[i]+sticker[i+2])

    return max(sticker)

def solution(sticker):
    
    if len(sticker) < 3: return max(sticker)
    
    return max(dp(sticker[:-1]), dp(sticker[1:])) # 첫 번째 스티커를 포함한 범위와 마지막 스티커를 포함한 범위에서 구한 최댓값 중 큰 값