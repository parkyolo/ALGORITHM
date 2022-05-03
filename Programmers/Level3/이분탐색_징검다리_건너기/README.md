## 징검다리 건너기
### 문제
https://programmers.co.kr/learn/courses/30/lessons/64062  

### 풀이
- 이분 탐색
- 이분 탐색의 범위 설정
    - start + 1 < end인 동안 mid = (start + end) // 2
    - 계산된 값이 정답의 범위에 들어온다면, start = mid
    - 아니라면 end = mid
    - return start