## LCS
### 문제
https://www.acmicpc.net/problem/9251  
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

### 풀이
- 최장 공통 부분 수열 문제
- A[i] == B[j]일 땐 지금까지의 최장 공통 부분 수열의 길이(```dp[i-1][j-1]```)에 + 1
- A[i] != B[j]일 땐 이전까지의 최장 공통 부분 수열의 길이(```max(dp[i-1][j], dp[i][j-1])```)의 값을 넣어줌