## 햄버거 분배

### 문제
기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다. 사람들은 자신의 위치에서 거리가 $K$ 이하인 햄버거를 먹을 수 있다.

햄버거	사람	햄버거	사람	햄버거	사람	햄버거	햄버거	사람	사람	햄버거	사람
1	2	3	4	5	6	7	8	9	10	11	12
위의 상태에서 $K = 1$인 경우를 생각해보자. 이 경우 모든 사람은 자신과 인접한 햄버거만 먹을 수 있다. 10번의 위치에 있는 사람은 11번 위치에 있는 햄버거를 먹을 수 있다. 이 경우 다음과 같이 최대 5명의 사람이 햄버거를 먹을 수 있다.

- 2번 위치에 있는 사람: 1번 위치에 있는 햄버거
- 4번 위치에 있는 사람: 5번 위치에 있는 햄버거
- 6번 위치에 있는 사람: 7번 위치에 있는 햄버거
- 9번 위치에 있는 사람: 8번 위치에 있는 햄버거
- 10번 위치에 있는 사람: 11번 위치에 있는 햄버거
- 12번 위치에 있는 사람: 먹을 수 있는 햄버거가 없음

 $K = 2$인 경우에는 6명 모두가 햄버거를 먹을 수 있다.

- 2번 위치에 있는 사람: 1번 위치에 있는 햄버거
- 4번 위치에 있는 사람: 3번 위치에 있는 햄버거
- 6번 위치에 있는 사람: 5번 위치에 있는 햄버거
- 9번 위치에 있는 사람: 7번 위치에 있는 햄버거
- 10번 위치에 있는 사람: 8번 위치에 있는 햄버거
- 12번 위치에 있는 사람: 11번 위치에 있는 햄버거
식탁의 길이 $N$, 햄버거를 선택할 수 있는 거리 $K$, 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램을 작성하시오.

### 입력
첫 줄에 두 정수 $N$과 $K$가 있다. 그리고 다음 줄에 사람과 햄버거의 위치가 문자 P(사람)와 H(햄버거)로 이루어지는 길이 $N$인 문자열로 주어진다.

### 출력
첫 줄에 햄버거를 먹을 수 있는 최대 사람 수를 나타낸다.

### 문제풀이
- 사람과 햄버거의 위치를 각각 배열에 저장
- 사람을 기준으로 햄버거가 k 위치 안에 있을 경우 cnt += 1
    - 먹은 햄버거는 -1로 표시해줌
    - 사람을 기준으로 앞의 햄버거를 먼저 확인하고 없을 경우 뒤도 확인
    - 앞의 햄버거는 앞에 있는 사람이 먹지 못하면 뒤에 있는 사람도 먹지 못하기 때문