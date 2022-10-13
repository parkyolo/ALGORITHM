def play():
    N = int(input())
    cards = list(map(int, input().split()))

    score = [[0 for _ in range(N)] for _ in range(N)] # score[i][j] : i번부터 j번까지의 카드가 남아있을 때 근우가 선택할 수 있는 최대 점수

    turn = True if N % 2 else False # True이면 근우 차례
    
    for length in range(N): # 남아있는 길이
        for i in range(N-length):
            if length == 0: # 카드가 한 장 남았을 때
                score[i][i] = cards[i] if turn else 0 # 근우 차례이면 근우의 점수가 되고 아니면 0점
            elif turn:      # 근우 차례일 때
                score[i][i+length] = max(score[i+1][i+length]+cards[i], score[i][i+length-1]+cards[i+length])
            else:           # 명우 차례일 때
                score[i][i+length] = min(score[i+1][i+length], score[i][i+length-1])
        turn = not turn

    print(score[0][N-1])            

    
def main():
    T = int(input())
    for _ in range(T):
        play()


if __name__ == "__main__":
    main()