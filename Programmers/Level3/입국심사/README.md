## 입국심사
### 문제
https://programmers.co.kr/learn/courses/30/lessons/43238
### 풀이
- 이분탐색 문제
- end는 최대로 걸릴 수 있는 심사 시간 (심사하는데 걸리는 시간이 가장 긴 심사관에게 모두 심사받는 경우)
- mid분 동안 모든 심사대에서 심사받을 수 있는 총 인원 수가 n명이 넘으면 right = mid - 1
- n명이 넘지 않으면 left = mid + 1