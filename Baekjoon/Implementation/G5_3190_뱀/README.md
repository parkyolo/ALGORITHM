## 뱀
### 문제
https://www.acmicpc.net/problem/3190  

### 풀이
- 뱀의 위치를 queue에 저장
    - 뱀의 머리를 queue에 추가, 뱀이 사과를 먹지 않았을 때 꼬리를 popleft()
- 뱀이 N*N의 범위를 벗어나거나 queue에 있는 위치(뱀의 몸)에 도달했을 때 종료