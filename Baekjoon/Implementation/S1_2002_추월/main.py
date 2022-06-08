N = int(input())
dictionary = {input():i for i in range(1, N+1)}
nums = [dictionary[input()] for _ in range(N)]
answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        if nums[i] > nums[j]:
            answer += 1
            break

print(answer)

"""
최장 증가 부분 수열 문제인 줄 알았지만 아니었다,,

"""
# seq = [nums[0]]

# def binary_search(start, end, target):
#     while start < end:
#         mid = (start + end) // 2
#         if seq[mid] > target: end = mid
#         else: start = mid+1
#     return end

# for i in range(1, N):
#     if nums[i] > seq[-1]: seq.append(nums[i])
#     else:
#         idx = binary_search(0, len(seq), nums[i])
#         seq[idx] = nums[i]

# # print(seq)
# print(N-len(seq))