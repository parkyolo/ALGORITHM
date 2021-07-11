import heapq

def solution(operations):
    answer = []
    heap = []
    
    for i in range(len(operations)):
        oper, num = operations[i].split()
        # 명령어가 "I 숫자"일 때 heap에 숫자를 push
        if oper == "I":
            heapq.heappush(heap, int(num))
        elif oper == "D":
            if heap:
                # 명령어가 "D -1"일 때 heap에서 min 값을 삭제
                if num == '-1':
                    heap.remove(min(heap))
                # 명령어가 "D 1"일 때 heap에서 max 값을 삭제
                elif num == '1':
                    heap.remove(max(heap))

    # heap이 비어있지 않을때 max값과 min값을 return
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
        
    return answer