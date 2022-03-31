## N-Queen
### 문제
https://www.acmicpc.net/problem/9663
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

### 출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

### 풀이
- https://chanhuiseok.github.io/posts/baek-1/ 블로그, https://www.acmicpc.net/board/view/64593 답변 참고
- 1차원 배열의 i번째 값 j는 체스판에서 i열j행에 퀸을 놓았다는 것을 의미
- 1차원 배열의 i번째 값과 m번째 값이 abs(m-i)만큼 차이난다면 대각선상에 위치한다는 의미이므로 패스
- 1차원 배열에서 값이 하나라도 같다면, 열의 위치가 같다는 것이기 때문에 방문한 열을 체크해서 v[i] = True라면 continue
- dfs로 nqueen을 호출해서 m이 n이 되면 cnt += 1