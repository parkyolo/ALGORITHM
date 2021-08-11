def solution(numbers):
    answer = []

    for n in numbers:

        if n%2==0 :
            answer.append(n+1)
        else:
            bit = list('0'+bin(n)[2:])
            index_0 = 0
            for i in range(len(bit)-1, -1, -1):
                if bit[i] == '0':
                    index_0 = i
                    break
            bit[index_0] = '1'
            bit[index_0+1] = '0'

            answer.append(int(''.join(bit), 2))

    return answer

print(solution([2,3,7,9]), [3,5,11,10])