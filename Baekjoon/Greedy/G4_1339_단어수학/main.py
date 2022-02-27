n = int(input())
words = [input() for _ in range(n)]
nums = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
apb_cnt = {} # 알파벳의 숫자와 곱해지는 크기 cnt
for word in words:
    for i, s in enumerate(word):
        if apb_cnt.get(s):
            apb_cnt[s] += 10**(len(word)-i)
        else:
            apb_cnt[s] = 10**(len(word)-i)
# print(apb_cnt)
sorted_num = sorted(apb_cnt.items(), key= lambda x: -x[1]) # 크기가 큰 순서대로 정렬
# print(sorted_num)
str_to_num = {a[0]:num for a, num in zip(sorted_num, nums)} # 9부터 숫자 할당
# print(str_to_num)
result = 0
for word in words:
    s_num = ''
    for s in word:
        s_num += str_to_num[s]
    result += int(s_num)
print(result)