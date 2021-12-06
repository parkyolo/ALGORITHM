n = int(input())
memory = list(map(int, input().split()))

order = [str(n)]
for i in range(n-2, -1, -1):
    # 앞에 memroy[i]명의 사람이 올 수 있도록 슬라이싱
    order = order[:memory[i]] + [str(i+1)] + order[memory[i]:]

print(' '.join(order))