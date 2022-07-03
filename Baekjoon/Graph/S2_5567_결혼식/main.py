def main():
    n = int(input())
    m = int(input())
    graph = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    answer = set()
    for j in graph[1]:
        answer.add(j)
        for k in graph[j]:
            answer.add(k)
    
    print(max(len(answer)-1, 0))

if __name__ == "__main__":
    main()