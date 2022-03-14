n, m = map(int, input().split())

def count_factors(n, f): # n에 f가 몇 개 있는지 count
    cnt = 0
    while n:
        cnt += n//f
        n //= f
    return cnt

n_cnt_two = count_factors(n, 2)
m_cnt_two = count_factors(m, 2)
n_m_cnt_two = count_factors(n-m, 2)

n_cnt_five = count_factors(n, 5)
m_cnt_five = count_factors(m, 5)
n_m_cnt_five = count_factors(n-m, 5)

print(min(n_cnt_two-(m_cnt_two+n_m_cnt_two), n_cnt_five-(m_cnt_five+n_m_cnt_five)))