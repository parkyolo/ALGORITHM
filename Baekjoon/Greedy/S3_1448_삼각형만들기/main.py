import sys

input = sys.stdin.readline

def main():
    N = int(input())
    straw = list(int(input()) for _ in range(N))
    straw.sort(reverse=True)
    for i in range(N-2):
        if straw[i] < straw[i+1] + straw[i+2]: # 삼각형의 조건
            print(straw[i] + straw[i+1] + straw[i+2])
            return
    print(-1)
    return
                

if __name__ == "__main__":
    main()