N, S, cnt = 0, 0, 0
seq = []

def get_sub_seq(sub_seq, k, sum_):
    global cnt
    if len(sub_seq) and sum_ == S: cnt += 1

    for i in range(k, N):
        if i in sub_seq: continue
        sub_seq.append(i)
        sum_ += seq[i]
        get_sub_seq(sub_seq, i+1, sum_)
        sub_seq.pop()
        sum_ -= seq[i]

def main():
    global N, S, seq
    N, S = map(int, input().split())
    seq = list(map(int, input().split()))
    get_sub_seq([], 0, 0)

    print(cnt)

if __name__ == "__main__":
    main()