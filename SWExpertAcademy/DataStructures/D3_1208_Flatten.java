/*
 * 1. summary: 문제 해석
 * 가장 높은 상자에서 1을 빼고, 가장 낮은 상자에 1을 더하면서 가장 높은 곳과 가장 낮은 곳의 차이가 1 이내가 되도록 하는 만든다.
 * 주어진 횟수만큼 위의 행동을 반복하고 최고점과 최저점의 차이를 출력한다.
 * 
 * 2. strategy: 풀이전략
 * boxs 배열에 높이를 저장한다.
 * boxs 배열을 정렬하여 최댓값과 최솟값의 차이를 구한다.
 * 최댓값과 최솟값의 차가 2 이상이면 최댓값엔 1을 빼고, 최솟값엔 1을 더한다.
 * 
 * 3. note: 주의할 사항(특이사항)
 */

import java.util.Arrays;
import java.util.Scanner;

public class SWEA1208_Flatten {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = 10;
        
        for(int test_case = 1; test_case <= T; test_case++) {
            int cnt = sc.nextInt();
            int[] boxs = new int[100];
            
            for (int i = 0; i < 100; i++) {
                boxs[i] = sc.nextInt();
            }
            
            
            for (int i = 0; i < cnt; i++) {
                Arrays.sort(boxs);
                if (boxs[99] - boxs[0] < 2) {
                    break;
                }
                
                boxs[0] += 1;
                boxs[99] -= 1;
            }
            
            Arrays.sort(boxs);
            int result = boxs[99] - boxs[0];
            
            System.out.println("#" + test_case + " " + result);
        }
        
        sc.close();
    }

}
