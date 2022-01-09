## 모두 0으로 만들기
### 문제 설명
https://programmers.co.kr/learn/courses/30/lessons/76503
### 문제 풀이
- leaf node부터 root node까지 ```a[node]```에 가중치를 더해주면서 가중치의 절댓값을 ```cnt```에 더해줌
- leaf node부터 계산해줘야하기 때문에 dfs로 풀이
- ```0```을 root로 설정