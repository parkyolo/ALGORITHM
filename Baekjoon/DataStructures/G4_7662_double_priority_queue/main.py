import math

def push_down_min(heap, i): # 아래에 있는 min level의 값과 비교해서 최솟값을 갱신
    if len(heap) > i*2+1: # i has children
        m = i*2+1
        if i*2+2 < len(heap) and heap[i*2+2] < heap[m]:
            m += 1
        grandchild = False
        for j in range(i*4+3, min(i*4+7, len(heap))):
            if heap[j] < heap[m]:
                m = j
                grandchild = True
        if grandchild:
            if heap[m] < heap[i]:
                heap[m], heap[i] = heap[i], heap[m]
                if heap[m] > heap[(m-1)//2]:
                    heap[m], heap[(m-1)//2] = heap[(m-1)//2], heap[m]
                push_down_min(heap, m)
        elif heap[m] < heap[i]:
            heap[m], heap[i] = heap[i], heap[m]

def push_down_max(heap, i): # 아래에 있는 max level의 값과 비교해서 최댓값을 갱신
    if len(heap) > i*2+1: # i has children
        m = i*2+1
        if i*2+2 < len(heap) and heap[i*2+2] > heap[m]:
            m += 1
        grandchild = False
        for j in range(i*4+3, min(i*4+7, len(heap))):
            if heap[j] > heap[m]:
                m = j
                grandchild = True
        if grandchild:
            if heap[m] > heap[i]:
                heap[m], heap[i] = heap[i], heap[m]
                if heap[m] < heap[(m-1)//2]:
                    heap[m], heap[(m-1)//2] = heap[(m-1)//2], heap[m]
                push_down_max(heap, m)
        elif heap[m] > heap[i]:
            heap[m], heap[i] = heap[i], heap[m]

def push_down(heap, i):
    level = int(math.log(i+1, 2))
    if level % 2 == 0: # min level
        push_down_min(heap, i)
    else: # max level
        push_down_max(heap, i)

def remove_min(heap): # 최솟값 삭제 연산
    """
    가장 마지막 값을 pop하고 temp에 저장한 후
    root(최솟값)에 temp를 넣어줌
    temp의 실제 자리를 찾기 위해 push_down
    """
    temp = heap.pop()
    heap[0] = temp
    push_down(heap, 0)

def remove_max(heap): # 최댓값 삭제 연산
    """
    가장 마지막 값을 pop하고 temp에 저장한 후
    root의 자식 노드 중 큰 값(최댓값)에 temp를 넣어줌
    temp의 실제 자리를 찾기 위해 push_down
    """
    if len(heap) < 3:
        heap.pop()
        return
    elif len(heap) == 3:
        temp = min(heap[1], heap[2])
        heap.pop()
        heap[1] = temp
        return
    idx = 1 if heap[1] > heap[2] else 2
    temp = heap.pop()
    heap[idx] = temp
    push_down(heap, idx)

def push_up_min(heap, i): # 위에 있는 min level의 값과 비교해서 최솟값을 갱신
    grandparent = (((i-1)//2)-1)//2
    if grandparent >= 0:
        if heap[i] < heap[grandparent]:
            heap[i], heap[grandparent] = heap[grandparent], heap[i]
            push_up_min(heap, grandparent)

def push_up_max(heap, i): # 위에 있는 max level의 값과 비교해서 최댓값을 갱신
    grandparent = (((i-1)//2)-1)//2
    if grandparent >= 0:
        if heap[i] > heap[grandparent]:
            heap[i], heap[grandparent] = heap[grandparent], heap[i]
            push_up_max(heap, grandparent)

def insertion(heap, key): # 삽입 연산
    """
    min value --> even level ex) 0, 2, 4, ...
    max value --> odd level ex) 1, 3, 5, ...
    root : min-max heap의 최솟값
    key : min-max heap에서 cur를 결정하는 값
    """
    heap.append(key)
    cur = len(heap)-1
    parent = (cur-1)//2
    if cur == 0: return # root node일 때
    level = int(math.log(cur+1, 2))
    if level % 2 == 0: # min level일 때
        if heap[cur] > heap[parent]: # 부모는 max level이고, max level보다 현재 key가 더 크다면
            heap[cur], heap[parent] = heap[parent], heap[cur] # 두 값을 swap
            push_up_max(heap, parent) # 부모 값이 max가 되는 위치로 올려 줌
        else:
            push_up_min(heap, cur) # 부모 값이 min이 되는 위치로 올려 줌
    else: # max level일 때
        if heap[cur] < heap[parent]:
            heap[cur], heap[parent] = heap[parent], heap[cur]
            push_up_min(heap, parent)
        else:
            push_up_max(heap, cur)

def main():
    T = int(input())
    for _ in range(T):
        heap = []
        k = int(input())
        for _ in range(k):
            cmd, n = input().split()
            if cmd == "D" and len(heap):
                if len(heap) == 1: heap.pop()
                else:
                    if n == "1": remove_max(heap)
                    else: remove_min(heap)
            elif cmd == "I": insertion(heap, int(n))
        
        if len(heap):
            if len(heap) <= 3:
                print(max(heap), heap[0])
            else:
                print(max(heap[1], heap[2]), heap[0])
        else: # heap이 비어있을 때
            print("EMPTY")

if __name__ == "__main__":
    main()