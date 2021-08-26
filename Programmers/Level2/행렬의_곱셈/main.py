def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        
        for j in range(len(arr2[0])): 
            su = 0
            for k in range(len(arr2)): 
                su += arr1[i][k] * arr2[k][j]
            temp.append(su)

        answer.append(temp)
        
    return answer

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]),[[15, 15], [15, 15], [15, 15]])
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]),[[22, 22, 11], [36, 28, 18], [29, 20, 14]])