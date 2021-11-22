n = int(input())
seq = list(map(int, input().split()))
x = int(input())
seq.sort() # 수열을 오름차순으로 정렬
answer = 0
end = n-1 # seq[i]와 더했을 때 x보다 작거나 같은 수
for i in range(n-1,0,-1):
    if seq[i] + seq[0] <= x:
        end = i
        break
# i는 가장 작은 수부터
# j는 end부터 i+1까지 (seq[i]와 더했을 때 x보다 작거나 같은 수만 확인)
for i in range(n):
    for j in range(end,i,-1):
        if seq[i] + seq[j] == x:
            answer += 1
            end = j
            break
print(answer)