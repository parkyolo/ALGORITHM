n, m = map(int, input().split())
not_heard = set() # 듣도 못한 사람
never_heard = [] # 듣도 보도 못한 사람

for _ in range(n):
    not_heard.add(input())
for _ in range(m):
    not_seen = input() # 보도 못한 사람
    if not_seen in not_heard:
        never_heard.append(not_seen)

never_heard.sort() # 사전순 정렬
print(len(never_heard))
for dbj in never_heard:
    print(dbj)