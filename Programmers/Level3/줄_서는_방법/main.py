answer = []

def lineup(n, k, nums, factorial):
    global answer
    if n == 1: return answer.append(nums[0])
    index = k // factorial[n-1]
    next_k = k % factorial[n-1]
    if next_k == 0: answer.append(nums.pop(index-1))
    else: answer.append(nums.pop(index))
    lineup(n-1, next_k, nums, factorial)

def solution(n, k):
    global answer
    answer = []
    nums = [i for i in range(1, n+1)]
    factorial = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        factorial[i] = factorial[i-1]*i
    lineup(n, k, nums, factorial)

    return answer

print(solution(4, 24), [4, 3, 2, 1])
print(solution(3, 3), [2, 1, 3])
print(solution(3, 5), [3, 1, 2])