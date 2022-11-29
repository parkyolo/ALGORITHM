n = int(input())

matrix = [[1, 1], [1, 0]]
unit = [[1, 1], [1, 0]]


def square(m1, m2):
    global matrix

    temp = [[0, 0], [0, 0]]
    
    for i in range(2):          # m1의 행
        for j in range(2):      # m2의 열
            for k in range(2):  # m1의 열, m2의 행
                # i*k x k*j -> i*j
                temp[i][j] += m1[i][k] * m2[k][j]
                temp[i][j] %= 1000000
    
    matrix = temp


def divide(x):
    if x == 1: return

    # A^n = (A^(n//2))*(A^(n//2))
    divide(x//2)
    square(matrix, matrix)

    if x % 2 == 1:  # x가 홀수일 때
        # A^n = A*(A^(n//2))*(A^(n//2))
        # A == unit
        square(matrix, unit)


if n > 1: divide(n-1)
print(matrix[0][0])