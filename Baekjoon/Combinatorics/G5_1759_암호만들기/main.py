L, C = map(int, input().split())
alphabets = input().split()
v = [0 for _ in range(C)]

alphabets.sort() # 알파벳 정렬

def check():
    vo, co = 0, 0 # 모음 수, 자음 수
    for i in range(C):
        if v[i]:
            if alphabets[i] in ['a', 'e', 'i', 'o', 'u']: vo += 1
            else: co += 1

    if vo >= 1 and co >= 2:
        return 1
    return 0

def comb(k): # 조합 구하기
    if sum(v) == L: # 길이가 L이면
        if check(): # 모음이 1개 이상, 자음이 2개 이상인지 검사
            print(''.join([alphabets[i] if v[i] else '' for i in range(C)]))
        return
    
    for i in range(k, C):
        if not v[i]:
            v[i] = 1
            comb(i)
            v[i] = 0

comb(0)