def solution(N, number):

    if N == number:
        return 1

    S = [0, {N}]
    for i in range(2, 9):
        sub_S = {int(str(N)*i)}
        for j in range(1, i//2+1): # N=3일 때 부분집합은 N=1, N=2 일 때와 N=2, N=1 일 때가 중복되기 때문에 절반만 연산함 

            # 집합의 모든 원소끼리 연산
            for x in S[j]:
                for y in S[i-j]:
                    sub_S.add(x+y)
                    sub_S.add(x-y)
                    sub_S.add(y-x) # 반대로 빼기 연산을 하는 케이스 추가
                    sub_S.add(x*y)
                    if x != 0:
                        sub_S.add(y//x)
                    if y != 0:
                        sub_S.add(x//y)

        if number in sub_S:
            return i

        S.append(sub_S)

    return -1

# print(solution(2, 11), 3)
print(solution(5, 12), 4)