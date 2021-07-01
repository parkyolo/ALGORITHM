def solution(number, k):
    answer = ''

    stack = []
    for num in number:
        # num이 앞의 수보다 크고 아직 k개를 다 제거하지 않았다면,
        # 앞의 수를 제거하고 k -= 1
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 k개를 다 제거하지 못했을 경우
    # stack에서 더 높은 자리 수 len(stack)-k개를 return
    for num in stack[:len(stack)-k]:
        answer += num

    return answer