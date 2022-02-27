from itertools import combinations

n = int(input())
nums = list()

for i in range(1, 11): # 1자리 수부터 10자리 수까지 0~9의 n자리 수 조합을 만듦
    for comb in combinations(range(0,10), i):
        comb = list(comb)
        comb.sort(reverse=True) # n자리 수 조합을 감소하는 수로 정렬
        nums.append(int("".join(map(str, comb))))

nums.sort() # 오름차순으로 정렬

try:
    print(nums[n]) # nums 배열의 n번째 숫자를 출력
except:
    print(-1)