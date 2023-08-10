/*
 * 1. summary
 * 규영이와 인영이가 1부터 18까지의 숫자가 적힌 카드를 9장씩 나눈다.
 * 규영이가 내는 카드의 순서가 주어진다.
 * 인영이가 카드를 내는 9!가지의 순서에 따라 규영이가 이기는 경우와 지는 경우가 총 몇 가지인지 구한다.
 * 
 * 2. strategy
 * next permutation을 활용하여 인영이가 카드를 내는 9!가지의 순서를 구한다.
 * 모든 경우의 수마다 규영이의 승패 여부를 count한다.
 * 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D3_6808_CardGame {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int[] GY = new int[9];
			int[] IY = new int[9];
			
			boolean[] num = new boolean[19];
			for (int i = 0; i < 9; i++) {	// 1. 규영이의 카드 입력받기
				GY[i] = Integer.parseInt(st.nextToken());
				num[GY[i]] = true;
			}
			
			int idx = 0;
			for (int i = 1; i <= 18; i++) {	// 2. 인영이의 카드를 오름차순으로 저장
				if (!num[i]) {
					IY[idx++] = i;
				}
			}
			
			int[] result = new int[3];	// result[0]: 규영이가 이기는 경우, result[1]: 규영이가 지는 경우
			do {
				result[play(GY, IY)] ++;	// 게임 play (점수 계산)
			} while (np(IY));				// 순열 구하기
			
			System.out.println("#" + test_case + " " + result[0] + " " + result[1]);
			
		}
	}
	
	private static boolean np(int[] perm) {
		int i = 8;
		while (i > 0 && perm[i-1] >= perm[i]) --i;
		
		if (i == 0) return false;
		
		int j = 8;
		while (perm[i-1] >= perm[j]) --j;
		
		swap(perm, i-1, j);
		
		int k = 8;
		while (i < k) {
			swap(perm, i++, k--);
		}
		
		return true;
	}
	
	private static void swap(int[] perm, int a, int b) {
		int temp = perm[a];
		perm[a] = perm[b];
		perm[b] = temp;
	}
	
	private static int play(int[] GY, int[] IY) {
		int scoreGY = 0;
		int scoreIY = 0;
		
		// 높은 수가 적힌 카드를 낸 사람은 두 카드에 적힌 수의 합만큼 접수를 얻는다.
		for (int i = 0; i < 9; i++) {
			if (GY[i] > IY[i]) {
				scoreGY += GY[i] + IY[i];
			} else {
				scoreIY += GY[i] + IY[i];
			}
		}
		
		if (scoreGY > scoreIY) {
			return 0;
		} else if (scoreGY < scoreIY) {
			return 1;
		} else {
			return 2;
		}
	}

}
