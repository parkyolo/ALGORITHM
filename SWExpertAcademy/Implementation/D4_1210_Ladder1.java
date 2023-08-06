/*
 * 1. summary: 문제 해석
 * 0과 1로 이루어진 2차원 배열에서 2로 표시된 x좌표에서 시작하여 1을 따라 올라갔을 때 도착하는 지점 찾기
 * 
 * 2. strategy: 풀이전략
 * 현재 위치를 0으로 변경하면서 방문 체크를 한다.
 * 현재 위치에서 왼쪽과 오른쪽에 1이 있는지 먼저 검사하고 있으면 그 위치로 이동한다.
 * 왼쪽 오른쪽이 모두 1이 아니면, 위로 이동한다.
 * y좌표가 -1이 될 때까지 반복한다.
 * 
 * 3. note: 주의할 사항(특이사항)
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D4_1210_Ladder1 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = 10;
        int test_case = 0;
        
        while (test_case < T) {
            test_case = Integer.parseInt(br.readLine());
        
            int[][] ladder = new int[100][100];
            int cy = 99, cx = 0;
            
            for (int i = 0; i < 100; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    ladder[i][j] = Integer.parseInt(st.nextToken());
                    if (i == 99 && ladder[99][j] == 2) {
                        cx = j;
                    }
                }
            }

            while (cy > -1) {
                ladder[cy][cx] = 3;
                if (cx - 1 >= 0 && ladder[cy][cx-1] == 1) {
                    cx --;
                } else if (cx + 1 < 100 && ladder[cy][cx+1] == 1) {
                    cx ++;
                } else {
                    cy --;
                }
            } 
            
            System.out.println("#" + test_case + " " + cx);
        }

    }

}
