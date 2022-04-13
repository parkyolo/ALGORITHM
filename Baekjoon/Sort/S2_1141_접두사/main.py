n = int(input())
words = []
for i in range(n):
    words.append(input())
words.sort() # 접두사는 무조건 단어보다 길이가 짧으므로 길이순으로 정렬한 후 뒤의 단어와만 비교한다.
answer = n
for i in range(n-1):
    e = words[i]
    for j in range(i+1, n):
        if words[j][:len(e)] == e:
            answer -= 1 # 다른 단어의 접두사가 되면 제거
            break
print(answer)