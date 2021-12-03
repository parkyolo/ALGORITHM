c = list(map(int, input().split()))
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def get_power(u): # 전투력 계산
    u_power = u[0] * (1+u[1]/100) * ((1-min(u[2]/100, 1)) + min(u[2]/100, 1) * u[3]/100) * (1+u[4]/100)
    return u_power

# 무기를 바꾸기 전의 전투력
c_before = get_power(c)
p_before = get_power(p)

# print(c_before)
# print(p_before)

# 무기 바꾸기
for i in range(5):
    c[i] = c[i] - a[i] + b[i]
    p[i] = p[i] - b[i] + a[i]

# 무기를 바꾼 후의 전투력
c_after = get_power(c)
p_after = get_power(p)

# print(c_after)
# print(p_after)

# 전투력 비교
if c_after < c_before: print("-")
elif c_after == c_before: print("0")
else: print("+")

if p_after < p_before: print("-")
elif p_after == p_before: print("0")
else: print("+")