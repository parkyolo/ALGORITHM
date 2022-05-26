## 최솟값
### 문제
https://www.acmicpc.net/problem/10868
### 풀이
https://github.com/parkyolo/Algorithm/tree/master/Baekjoon/DataStructures/G1_2357_최솟값과최댓값 과 유사한 문제
- Segment Tree를 이용해 풀이
- M개의 a, b 쌍을 입력받는 과정에서 input을 쓰면 시간 초과가 남  
    --> sys.stdin.readline()을 쓰면 해결  
    - input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
