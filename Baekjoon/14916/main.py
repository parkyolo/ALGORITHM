n = int(input())

# n이 5로 나누어 떨어질 때
if n % 5 == 0:
    print(n // 5)

# n이 5보다 클 때
elif n > 5:
    cnt = n // 5
    # 5원 짜리를 최대로 낼 수 있을 때
    if (n - cnt * 5) % 2 == 0:
        cnt += (n - cnt * 5) // 2
    # 5원 짜리를 최대로 낼 수 없을 때
    else:
        cnt -= 1
        cnt += (n - cnt * 5) // 2
    print(cnt)

# n이 5보다 작을 때
elif n < 5:
    # n이 2로 나누어 떨어질 때
    if n % 2 == 0:
        print(n//2)
    # 거슬러 줄 수 없는 경우
    else:
        print(-1)