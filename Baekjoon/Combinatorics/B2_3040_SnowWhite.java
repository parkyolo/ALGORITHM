/*
 * 1. summary
 * 9개의 숫자 중 합이 100이 되는 7개의 숫자를 출력한다.
 * 
 * 2. strategy
 * 9개의 숫자 중 7개의 숫자 조합을 구한다.
 * 7개의 숫자 합이 100이 되면 출력한다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B2_3040_SnowWhite {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] nums = new int[9];
		for (int i = 0; i < 9; i++) {
			nums[i] = Integer.parseInt(br.readLine());
		}
		
		combi(0, 0, 0, new int[7], nums);
	}
	
	public static void combi(int cnt, int start, int sum, int[] selected, int[] nums) {
		if (cnt == 7) {
			if (sum == 100) {
				for (int idx : selected) {
					System.out.println(nums[idx]);
				}
			}
			return;
		}
		
		for (int i = start; i < 9; i++) {
			selected[cnt] = i;
			combi(cnt+1, i+1, sum+nums[i], selected, nums);
		}
	}

}
