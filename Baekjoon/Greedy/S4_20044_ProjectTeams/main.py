n = int(input())
students = list(map(int, input().split()))
students.sort()
teams = [0 for _ in range(n)]
for i in range(n):
    teams[i] = students[i] + students[2*n-i-1]
print(min(teams))