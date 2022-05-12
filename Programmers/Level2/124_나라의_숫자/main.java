/*
- n을 3으로 나눈 나머지가 0일 땐 4, 1일 땐 1, 2일 땐 2에 대조된다.
- 수를 answer에 더해준 후, n-1을 3으로 나눈 값이 다음 n이 된다.
- 1의 자리 수부터 answer에 더해준 후 마지막에 뒤집는다.
*/

import java.lang.StringBuffer;

class Solution {
    public String solution(int n) {
        String answer = "";
        
        String[] num = {"4","1","2"};
        while (n > 0) {
            int m = n%3;
            answer += num[m];
            n = (n-1)/3;
        }
        
        StringBuffer sb = new StringBuffer(answer);
        String reverse_ans = sb.reverse().toString();
        return reverse_ans;
    }
}