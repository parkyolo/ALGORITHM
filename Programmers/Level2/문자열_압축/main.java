/*
- 문자열을 1개씩 자르는 경우부터 문자열의 길이/2개식 자르는 경우까지 탐색
- 압축한 문자열의 길이를 len에 저장
- 압축할 수 있는 개수를 same_cnt에 저장한 후 string으로 변환해서 same_cnt의 길이를 len에 더해줌
*/

class Solution {
    public int solution(String s) {
        int answer = s.length();
        for (int i=1; i<=s.length()/2; i++) {
            int len = i;
            int same_cnt = 1;
            for (int j=i; j<=s.length()-i; j+=i) {
                if (s.substring(j,j+i).equals(s.substring(j-i,j))) {
                    same_cnt ++;
                } else {
                    if (same_cnt > 1) {
                        String cnt = Integer.toString(same_cnt);
                        len += cnt.length();
                        same_cnt = 1;
                        
                    }
                    len += i;
                }
            }
            if (same_cnt > 1) {
                String cnt = Integer.toString(same_cnt);
                len += cnt.length();
            }
            len += s.length()%i;
            if (len < answer) answer = len;
        }
        return answer;
    }
}