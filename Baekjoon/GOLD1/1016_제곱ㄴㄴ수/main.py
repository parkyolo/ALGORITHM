_min, _max = map(int, input().split())
nums = [1 for _ in range(_min, _max+1)]
length = len(nums)
for i in range(2, int(_max**0.5)+1):
    for j in range(_min//(i*i), _max//(i*i)+1):
        if 0 <= i * i * j - _min <= length: nums[i * i * j - _min] = 0
print(sum(nums))