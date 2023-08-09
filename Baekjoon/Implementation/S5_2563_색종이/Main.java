/*
 * 1. summary
 * 가로, 세로가 100인 배열에 가로, 세로가 10인 정사각형이 채워진다.
 * (0, 0)에서의 가로, 세로 거리가 주어졌을 때, 채워진 배열의 넓이를 구한다.
 * 
 * 2. strategy
 * 가로, 세로가 떨어진 거리에서 10만큼을 1로 채운다.
 * 이중 포문으로 1인 칸의 수를 센다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int[][] board = new int[100][100];
		
		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int left = Integer.parseInt(st.nextToken());
			int right = Integer.parseInt(st.nextToken());
			
			for (int j = left; j < left+10; j++) {
				for (int k = right; k < right+10; k++) {
					board[j][k] = 1;
				}
			}
		}
		
		int cnt = 0;
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (board[i][j] == 1) {
					cnt++;
				}
			}
		}
		
		System.out.println(cnt);
	}

}
