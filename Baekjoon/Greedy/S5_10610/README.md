## 30

### 문제
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

### 입력
N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

### 출력
미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

### 풀이
- 30의 배수는 3의 배수이자 10의 배수이다.
- 숫자 중 0이 없으면 10의 배수가 될 수 없다.
- 모든 자릿수를 더한 값이 3의 배수이면, 그 수도 3의 배수이다.
- 따라서, 숫자에 0이 있고 모든 자릿 수를 더한 값이 3의 배수이면, 30의 배수이다.
- 숫자를 큰 순으로 나열하면 30의 배수 중 가장 큰 수가 된다.