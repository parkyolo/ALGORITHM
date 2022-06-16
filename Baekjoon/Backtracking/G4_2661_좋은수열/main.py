N = int(input())

def isGood(seq):
    for i in range(1, len(seq)//2+1): # 부분수열의 길이
        for j in range(len(seq)-i): # 인접한 부분 수열이 동일한지 검사
            if seq[j:j+i] == seq[j+i:j+2*i]:
                return False
    return True

"""
좋은 수열 중 작은 수를 출력해야 하기 때문에 처음 등장하는 좋은 수열을 출력하고 종료
"""
def get_seq(seq):
    if len(seq) == N:
        if isGood(seq):
            print(seq) # 길이가 N인 좋은 수열이면 출력
            exit()

    if isGood(seq): # 좋은 수열이면 다음 수
        get_seq(seq+"1")
        get_seq(seq+"2")
        get_seq(seq+"3")

get_seq("1")