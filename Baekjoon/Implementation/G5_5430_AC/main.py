def AC(p, nums_array):
    reversed = False
    for cmd in p:
        if cmd == "R": # 뒤집기
            reversed = not reversed
        elif cmd == "D": # 버리기
            if not len(nums_array): # 배열이 비었을 때
                return 'error'
            else:
                if reversed: # 뒤집혀있을 때
                    nums_array.pop() # 마지막 원소 제거
                else: # 뒤집혀있지 않을 때
                    nums_array.pop(0) # 첫 번째 원소 제거
    
    if reversed: nums_array.reverse() # 배열 뒤집기
    result = "["+",".join([str(i) for i in nums_array])+"]"
    return result

def main():
    T = int(input())
    for _ in range(T):
        p = input()
        _ = int(input())
        nums_array = input()

        if nums_array == "[]": nums_array = []
        else:
            nums_array = nums_array[1:-1]
            nums_array = nums_array.split(",")

        result = AC(p, nums_array)
        print(result)

if __name__ == "__main__":
    main()