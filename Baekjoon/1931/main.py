n = int(input())

meeting = []
for i in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x:x[0])
meeting.sort(key=lambda x:x[1])

end = 0
cnt = 0
for s, e in meeting:
    if s >= end:
        end = e
        cnt += 1
print(cnt)