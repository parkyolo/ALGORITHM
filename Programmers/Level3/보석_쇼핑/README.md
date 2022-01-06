## 보석 쇼핑
### 문제 설명
https://programmers.co.kr/learn/courses/30/lessons/67258
### 문제 풀이
- ```start```부터 ```i```까지의 보석의 수를 ```gems_cnt``` dictionary에 저장
- start 보석과 같은 보석이 나타나면, ```gems_cnt[gems[start]]```가 1이 될 때까지 ```start += 1```
- ```gems_cnt```의 모든 보석이 한 개 이상이고(배열에 모든 보석이 포함되었고), 구간의 길이가 최소일 때 ```answer``` 갱신