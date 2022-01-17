## 거스름돈
### 문제
https://programmers.co.kr/learn/courses/30/lessons/12907
### 풀이
- ```dp[j] (0 < j <= n)```는 dp원을 만들 수 있는 경우의 수
- ```dp[j]```는 ```j```보다 ```money[i] (0 <= i < len(money))```만큼 덜 더했을 때인 ```dp[j-money[i]]```를 더해준다.