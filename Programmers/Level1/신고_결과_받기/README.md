## 신고 결과 받기
### 문제
### 풀이
- ```reported_cnt``` dictionary : {user id : key user가 신고 당한 횟수}
- ```reported_user``` dictionary : {user id : key user가 신고한 user id}
- 위의 두 dictionary를 생성하고, ```id_list```의 user가 신고한 uesr id의 신고 횟수가 ```k```보다 크거나 같으면 ```cnt+1```해서 ```answer```배열에 넣어줌
