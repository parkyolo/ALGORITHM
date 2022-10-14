## 보물상자 비밀번호
### 문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

### 풀이
- 4개의 변에 n//4개자리의 16진수가 들어가게 되므로 n//4번 회전하면 시작할 때와 같은 위치가 된다.
- n//4번 시계 방향으로 회전(마지막 숫자가 맨 앞으로 옴)하면서 16진수를 10진수로 변환하고 우선순위 큐에 넣는다.
- 내림차순으로 정렬하기 위해 숫자에 마이너스를 붙여준다.
- 우선순위 큐 안의 숫자를 k-1번 pop하고 k번 숫자를 반환한다.