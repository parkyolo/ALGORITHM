/*
 * 1. summary 
 * R*C 격자에 '.'은 빈칸, 'x'는 건물로 정보가 주어진다.
 * 각 칸을 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결하여 파이프라인을 만들어야 한다.
 * 첫째 열에서 마지막 열을 잇는 파이프라인의 최대 개수를 출력한다.
 * 
 * 2. strategy
 * 첫번째 행부터 마지막 행까지 파이프라인을 연결한다.
 * 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선 순으로 빈 칸이 있는지 확인한다.
 * 빈 칸이 있다면 연결하고, 없다면 돌아간다.
 * 마지막 열에 도착하면 파이프라인의 개수를 추가한다.
 * 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	private static int r, c;
	private static int[][] dxy = {{-1, 1}, {0, 1}, {1, 1}};

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		char[][] map = new char[r][c];
		for (int i = 0; i < r; i++) {
			String line = br.readLine();
			for (int j = 0; j < c; j++) {
				map[i][j] = line.charAt(j);
			}
		}
		
		int cnt = 0;
		for (int i = 0; i < r; i++) {
			if (setPipe(i, 0, map)) {
				cnt ++;
			}
		}

		System.out.println(cnt);
	}

	private static boolean setPipe(int sr, int sc, char[][] map) {
		if (sc == c-1) return true;
		
		for (int i = 0; i < 3; i++) {
			int nr = sr + dxy[i][0], nc = sc + dxy[i][1];
			if (nr < 0 || nr >= r || nc < 0 || nc >= c) continue;
			if (map[nr][nc] == 'x') continue;
			map[nr][nc] = 'x';
			if(setPipe(nr, nc, map)) return true;
		}
		
		return false;
	}

}
