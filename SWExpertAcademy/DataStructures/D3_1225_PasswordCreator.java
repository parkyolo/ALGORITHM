/*
 * 1. summary: 문제 해석
 * 8개의 숫자를 입력받는다.
 * 첫 번째 숫자를 i(1<=i<=5)만큼 감소한 뒤, 맨 뒤로 보내는 사이클을 반복한다.
 * 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램이 종료된다.
 * 
 * 2. strategy: 풀이전략
 * queue에 입력받은 숫자를 넣는다.
 * 맨 앞의 숫자를 감소시킨 뒤, 맨 뒤에 삽입한다.
 * 맨 뒤의 숫자가 0보다 작아지면 종료한다.
 * 
 * 3. note: 주의할 사항(특이사항)
 * 테스트케이스는 10개이다.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class D3_1225_PasswordCreator {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for (int t = 0; t < 10; t++) {
            int test_case = Integer.parseInt(br.readLine());
            
            ArrayDeque<Integer> queue = new ArrayDeque<>();
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            for (int i = 0; i < 8; i++) {
                int num = Integer.parseInt(st.nextToken());
                queue.offer(num);
            }
            
            int decNum = 1;
            while (queue.peekLast() > 0) {
                queue.offer(Math.max(0, queue.poll() - decNum));
                decNum = decNum == 5 ? 1 : decNum + 1;				
            }
            
            System.out.print("#" + test_case + " ");
            while (!queue.isEmpty()) {
                System.out.print(queue.poll() + " ");
            }
            System.out.println();
        }
    }

}
