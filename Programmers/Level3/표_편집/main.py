def solution(n, k, cmd):
    linked_list = {i:[i-1, i+1] for i in range(n)}
    table = ["O" for _ in range(n)]
    stack = []
    for c in cmd:
        line = c.split()
        if line[0] == "D": # D 이후의 숫자만큼 이동
            for i in range(int(line[1])):
                k = linked_list[k][1]
        elif line[0] == "U": # U 이후의 숫자만큼 이동
            for i in range(int(line[1])):
                k = linked_list[k][0]
        elif line[0] == "C": # k를 stack에 넣고 table[k]에 "X" 표시
            stack.append([linked_list[k][0], k, linked_list[k][1]])
            table[k] = "X"

            # k의 이전 노드와 이후 노드를 이어줌
            if linked_list[k][0] == -1:
                linked_list[linked_list[k][1]][0] = linked_list[k][0]
            elif linked_list[k][1] == n:
                linked_list[linked_list[k][0]][1] = linked_list[k][1]
            else:
                linked_list[linked_list[k][0]][1] = linked_list[k][1]
                linked_list[linked_list[k][1]][0] = linked_list[k][0]
            
            # k값을 갱신
            if linked_list[k][1] == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]
        else:
            z = stack.pop() # stack에서 가장 최근에 지운 글자 z를 꺼냄
            table[z[1]] = "O" # table[z]에 "O" 표시
            # z에 이전 노드와 이후 노드를 다시 이어줌
            if z[0] == -1:
                linked_list[z[2]][0] = z[1]
            elif z[2] == n:
                linked_list[z[0]][1] = z[1]
            else:
                linked_list[z[0]][1] = z[1]
                linked_list[z[2]][0] = z[1]
            
                
    return ''.join(table)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]), "OOOOXOOO")
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]), "OOXOXOOO")