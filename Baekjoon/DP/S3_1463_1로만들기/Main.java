/*
 * 1. summary
 * 정수 X에 다음 세 가지 연산을 적절히 사용하여 1을 만드려고 한다.
 *  1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
 *  2. X가 2로 나누어 떨어지면, 2로 나눈다.
 *  3. 1을 뺀다.
 * 연산을 사용하는 횟수의 최솟값을 출력한다.
 * 
 * 2. strategy
 * 2부터 x까지 i를 3으로 나누었을 때, 2로 나누었을 때, 1을 뺐을 때 중 더 적은 연산을 사용하는 경우에 1을 더한다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int x = Integer.parseInt(br.readLine());
		
		int[] memo = new int[x+1];
		for (int i = 2; i <= x; i++) {
			int minCnt = Integer.MAX_VALUE;
			
			if (i % 3 == 0) minCnt = Math.min(minCnt, memo[i/3]);
			if (i % 2 == 0) minCnt = Math.min(minCnt, memo[i/2]);
			minCnt = Math.min(minCnt, memo[i-1]);
			
			memo[i] = minCnt+1;
		}

		System.out.println(memo[x]);
	}

}
