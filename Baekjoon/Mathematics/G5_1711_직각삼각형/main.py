import math

N, points = 0, []

def solution(std):
    cnt = 0
    temp = points
    points[0], points[std] = points[std], points[0]

    vectors = dict()
    for i in range(1, N):
        x, y = temp[i][0] - temp[0][0], temp[i][1] - temp[0][1]
        g = math.gcd(x, y) # x와 y의 최대공약수
        if g < 0: g = -g

        # 현재 기준이 되는 점과 i번째 점을 잇는 선을 단위벡터화
        x //= g
        y //= g

        # 동일한 벡터가 여러개일 수도 있기 때문에 개수를 저장
        if (x, y) in vectors: vectors[(x, y)] += 1
        else: vectors[(x, y)] = 1

    for key, val in vectors.items():
        cx, cy = key[0], key[1]
        if (-cy, cx) in vectors: # 직교하는 벡터가 있으면
            cnt += val * vectors[(-cy, cx)] # 벡터의 수만큼 count

    return cnt

def main():
    global N, points
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N): # 직각이 되는 한 점
        answer += solution(i) 

    print(answer)
    return

if __name__ == "__main__":
    main()