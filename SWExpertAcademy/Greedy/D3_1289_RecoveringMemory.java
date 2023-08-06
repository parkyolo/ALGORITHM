/*
 * 1. summary: 문제 해석
 * 왼쪽 bit부터 toggle하면서 0으로 이루어진 초기화 상태를 주어진 상태로 변경하는 문제
 * 
 * 2. strategy: 풀이전략
 * 값을 토글하면 오른쪽 값이 모두 변경되기 때문에 왼쪽부터 현재 비트를 그리디하게 토글한다.
 * 주어진 상태(input)의 i번째 값이 현재 상태(state)와 다르면 state를 토글하고 cnt를 증가시킨다.
 * 
 * 3. note: 주의할 사항(특이사항)
 */

import java.io.FileNotFoundException;
import java.util.Scanner;

public class SW1289_MemoryRecovery {

    public static void main(String[] args) throws FileNotFoundException {
        
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        
        for(int test_case = 1; test_case <= T; test_case++) {
            String input = sc.next();
            char state = '0';
            int cnt = 0;
            
            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) != state) {
                    state = (char)(1^state);
                    cnt++;
                }
            }
            
            System.out.println("#" + test_case + " " + cnt);
        }
        
        sc.close();
        
    }
    
}
