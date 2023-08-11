/*
 * 1. summary
 * 스네이크 버드는 과일을 먹으면 길이가 1만큼 늘어난다.
 * 스네이크 버드는 자신의 길이보다 작거나 같은 높이에 있는 과일만 먹을 수 있다.
 * 스네이크 버드의 길이와 과일이 높이가 주어질 때, 스네이크 버드의 최대 길이를 구한다.
 * 
 * 2. strategy
 * 과일을 오름차순으로 정렬한다.
 * 과일의 높이가 스네이크 버드의 길이보다 작거나 같으면 스네이크 버드의 길이를 늘린다.
 * 과일의 높이가 스네이크 버드의 길이보다 크면 탐색을 종료하고 스네이크 버드의 길이를 출력한다.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class S5_16435_SnakeBird {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		
		int[] fruits = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			fruits[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(fruits);
		for (int i = 0; i < n; i++) {
			if (fruits[i] <= l) {
				l ++;
			} else {
				break;
			}
		}
		
		System.out.println(l);
	}

}
