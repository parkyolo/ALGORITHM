## 불량 사용자
### 문제 설명
https://programmers.co.kr/learn/courses/30/lessons/64064
### 문제 풀이
1. user id 중 불량 사용자 id와 매핑되는 id를 ```off_id_dict[b_id]```에 추가
2. 각 불량 사용자의 제재 아이디 목록을 ```queue```에 담음
3. 제재 아이디가 중복되는 경우는 ```queue```에 담지 않음
4. 모든 불량 사용자의 제재 아이디가 하나씩 담겼을 때, 중복되지 않는 제재 아이디 목록만 ```result``` 배열에 추가