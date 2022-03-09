n = int(input())
seq = list(map(int, input().split()))
sub_seq = [seq[0]]

def binarySearch(target, start, end):
    while start < end:
        mid = (start+end)//2
        if target > sub_seq[mid]: start = mid
        else: end = mid
    return end

for i in range(1,n):
    if seq[i] > sub_seq[-1]:
        sub_seq.append(seq[i])
    else:
        idx = binarySearch(seq[i], 0, len(sub_seq)-1)
        sub_seq[idx] = seq[i]

print(len(sub_seq))