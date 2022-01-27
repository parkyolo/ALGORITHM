## 금과 은 운반하기
### 문제
https://programmers.co.kr/learn/courses/30/lessons/86053
### 풀이
- 광물을 운반하는 시간을 기준으로, 해당 시간동안 목표 무게를 운반할 수 있는지 확인하는 이분탐색 문제
- ```mid```시간동안 운반할 수 있는 금의 총 무게 ```total_g```와 은의 총 무게 ```total_s```를 구하고 금와 은을 더한 무게가 ```w[i]```보다 클 수도 있기 때문에 금과 은의 무게를 합친 무게 ```total```까지 구해서 ```total_g >= a and total_s >= b and total >= a+b```를 모두 만족하는 ```mid```를 찾아야한다.