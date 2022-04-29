N = int(input())
std = [1]+list(map(int, input().strip().split())) # 등급 기준액
grade = list(input()) # 받은 MVP 등급

amount = dict() # 등급 : 과금 기준액
score = ['B', 'S', 'G', 'P', 'D']
for i in range(5):
    amount[score[i]] = std[i]

upper_grade = {'B':'S', 'S':'G', 'G':'P', 'P':'D'} # 윗 등급
charge = [0 for _ in range(N)]

for i in range(1, N):
    if grade[i] == 'D': charge[i] = amount['D']
    elif i == 0:
        charge[i] = amount[upper_grade[grade[i]]] - 1 # 이번 달 등급보다 한 등급 높은 등급의 기준액 - 1
    else:
        charge[i] = amount[upper_grade[grade[i]]] - 1 - charge[i-1] # 이번 달 등급보다 한 등급 높은 등급의 기준액 - 1 - 지난 달 과금액

print(sum(charge))