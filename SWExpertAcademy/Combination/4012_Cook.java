/*
 * 1. summary
 * n개의 식재료를 n/2개씩 나누어 두 개의 요리를 한다.
 * 요리의 맛은 식재료 간의 시너지의 합이다.
 * 두 요리의 맛의 차이의 최솟값을 출력한다.
 * 
 * 2. strategy
 * 0부터 n-1까지의 숫자 중 n/2개를 뽑은 조합을 구한다. (foodA)
 * 위의 조합에 속하지 않은 숫자들로 두 번째 요리의 식재료를 구한다. (foodB)
 * 위에 구한 배열에서 원소 2개(i, j)로 이루어진 순열을 구한다.
 * synergy[i][j]의 합을 구한다.
 * foodA의 시너지 합과 foodB의 시너지 합의 차이의 최솟값을 구한다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 4012_Cook {
	private static int[][] synergy;
	private static int answer;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= t; test_case++) {
			int n = Integer.parseInt(br.readLine());
			
			synergy = new int[n][n];
			StringTokenizer st;
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					synergy[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			answer = Integer.MAX_VALUE;
			getCombi(n/2, 0, 0, new int[n/2]);
			
			System.out.println("#" + test_case + " " + answer);
		}
	}

	// 식재료 반으로 나누기
	private static void getCombi(int n, int cnt, int start, int[] selected) {
		if (cnt == n) {
			getSynergy(selected);
			return;
		}
		
		for (int i = start; i < n*2; i++) {
			selected[cnt] = i;
			getCombi(n, cnt+1, i+1, selected);
		}
	}
	
	// 두 음식의 시너지 차이 구하기
	private static void getSynergy(int[] foodA) {
		
		int n = foodA.length;
		boolean[] ingredients = new boolean[n*2];
		for (int i = 0; i < n; i++) {
			ingredients[foodA[i]] = true;
		}
		
		int[] foodB = new int[n];
		int idx = 0;
		for (int i = 0; i < n*2; i++) {
			if (!ingredients[i]) foodB[idx++] = i;
		}
		
		int synergyA = getPerm(n, 0, new int[2], foodA, new boolean[n]);
		int synergyB = getPerm(n, 0, new int[2], foodB, new boolean[n]);
		answer = Math.min(answer, Math.abs(synergyA - synergyB));
	}
	
	// 음식 하나에 대해 시너지 합 구하기
	private static int getPerm(int n, int cnt, int[] perm, int[] ingredients, boolean[] selected) {
		if (cnt == 2) {
			return synergy[perm[0]][perm[1]];
		}
		
		int sum = 0;
		for (int i = 0; i < n; i++) {
			if (selected[i]) continue;
			selected[i] = true;
			perm[cnt] = ingredients[i];
			sum += getPerm(n, cnt+1, perm, ingredients, selected);
			selected[i] = false;
		}
		
		return sum;
	}

}
