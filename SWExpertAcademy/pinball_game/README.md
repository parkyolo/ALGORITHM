## 핀볼 게임
### 문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo  
### 풀이
1. table[i][j] == 0일 때, 상하좌우로 움직이는 경우를 queue에 넣음
2. x, y가 출발위치로 돌아오거나 table[x][y] == -1이면 continue
3. 블록과 부딪히면 방향 전환, cnt+1
4. 웜홀과 만나면 반대쪽 웜홀로 위치 전환