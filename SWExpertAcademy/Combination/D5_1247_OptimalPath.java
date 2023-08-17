/*
 * 1. summary
 * 회사에서 출발하여 N명의 고객을 모두 방문하고 집으로 돌아오는 경로 중 가장 짧은 것을 찾는다.
 * 
 * 2. strategy
 * N명의 고객을 방문하는 순서에 대해 모든 경우의 수를 구한다.
 * 모든 경우의 수에 대해 거리를 구한다.
 * 거리가 지금까지 구한 최소 거리보다 길어지면 return한다.
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D5_1247_OptimalPath {
	
	private static int n, sr, sc, dr, dc, coord[][];
	private static int perm[];
	private static boolean isSelected[];
	private static int minDist;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= t; test_case++) {
			n = Integer.parseInt(br.readLine());
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			sr = Integer.parseInt(st.nextToken());	// 회사 좌표
			sc = Integer.parseInt(st.nextToken());
			dr = Integer.parseInt(st.nextToken());	// 집 좌표
			dc = Integer.parseInt(st.nextToken());
			
			coord = new int[n][2];	// 고객들 좌표
			for (int i = 0; i < n; i++) {
				coord[i][0] = Integer.parseInt(st.nextToken());
				coord[i][1] = Integer.parseInt(st.nextToken());
			}
			
			perm = new int[n];
			isSelected = new boolean[n];
			minDist = Integer.MAX_VALUE;
			getOrder(0);
			System.out.println("#" + test_case + " " + minDist);
		}
	}
	
	private static void getOrder(int cnt) {
		if (cnt == n) {
			getDist();
			return;
		}
		
		for (int i = 0; i < n; i++) {
			if (isSelected[i]) continue;
			isSelected[i] = true;
			perm[cnt] = i;
			getOrder(cnt+1);
			isSelected[i] = false;
		}
	}
	
	private static void getDist() {
		int dist = 0;
		
		int cr = sr, cc = sc;
		
		for (int i = 0; i < n; i++) {
			int nr = coord[perm[i]][0];
			int nc = coord[perm[i]][1];
			
			dist += Math.abs(cr-nr) + Math.abs(cc-nc);
			cr = nr;
			cc = nc;
			
			if (dist >= minDist) return;
		}
		
		dist += Math.abs(cr-dr) + Math.abs(cc-dc);
		
		minDist = Math.min(minDist, dist);
	}

}
