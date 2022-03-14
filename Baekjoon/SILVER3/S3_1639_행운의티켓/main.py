s = str(input())
n = len(s)
m = n if n % 2 == 0 else n - 1 # 부분문자열의 길이
while m:
    for i in range(n-m+1):
        sub_s = s[i:m+i] # 부분문자열
        if sum(list(map(int, list(sub_s[:m//2])))) == sum(list(map(int, list(sub_s[m//2:])))): # 왼쪽 N자리의 합과 오른쪽 N자리의 합이 일치하는지 확인
            print(m)
            exit()
    m -= 2

print(m)