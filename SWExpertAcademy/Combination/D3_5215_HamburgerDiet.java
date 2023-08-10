/*
 * 1. summary
 * 민기가 매긴 재료에 대한 점수와 가게에서 제공하는 재료의 칼로리가 주어진다.
 * 정해진 칼로리 이하의 조합 중 점수가 가장 높은 조합을 고른다.
 * 
 * 2. strategy
 * 재료에 대한 부분 집합을 구한다.
 * 부분 집합에 대해 점수와 칼로리를 계산한다.
 * 정해진 칼로리 이하일 때 점수의 최댓값을 구한다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D3_5215_HamburgerDiet {
	private static int n, l;
	private static int[] score, kcal;
	private static boolean[] isSelected;
	private static int answer;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());	// 재료의 수
			l = Integer.parseInt(st.nextToken());	// 제한 칼로리
			
			score = new int[n];
			kcal = new int[n];
			
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				score[i] = Integer.parseInt(st.nextToken());
				kcal[i] = Integer.parseInt(st.nextToken());
			}
			
			isSelected = new boolean[n];
			answer = 0;
			getSubSet(0);
			System.out.println("#" + test_case + " " + answer);
		}
	}
	
	private static void getSubSet(int cnt) {
		if (cnt == n) {
			getKcal();
			return;
		}
		
		isSelected[cnt] = true;
		getSubSet(cnt+1);
		isSelected[cnt] = false;
		getSubSet(cnt+1);
	}
	
	private static void getKcal() {
		int prefer = 0;
		int totalKcal = 0;
		for (int i = 0; i < n; i++) {
			if (isSelected[i]) {
				prefer += score[i];
				totalKcal += kcal[i];
			}
		}
		
		if (totalKcal <= l) {
			answer = Math.max(answer, prefer);
		}
	}

}
