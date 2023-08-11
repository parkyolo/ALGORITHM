/*
 * 1. summary
 * N*N 배열에 집과 치킨집의 위치가 주어진다.
 * 치킨집 중 M개를 뽑아서 가장 가까운 집과의 거리를 더했을 때 최솟값을 구한다.
 * 
 * 2. strategy
 * 집과 치킨집의 위치를 ArrayList에 저장한다.
 * 치킨집 중 M개의 조합을 구한다.
 * 집마다 가장 가까운 치킨집과의 거리(치킨 거리)를 구한다.
 * 치킨 거리의 합의 최솟값을 출력한다.
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class G5_15686_ChickenDelivery {
	private static int n, m;
	private static List<int[]> house;
	private static List<int[]> chicken;
	private static int answer;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		house = new ArrayList<int[]>();
		chicken = new ArrayList<int[]>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				int flag = Integer.parseInt(st.nextToken());
				if (flag == 1) {
					house.add(new int[] {i, j});
				} else if (flag == 2) {
					chicken.add(new int[] {i, j});
				}
			}
		}
		
		answer = Integer.MAX_VALUE;
		getCombi(0, 0, new int[m]);
		System.out.println(answer);
		
	}
	
	// 1. M개의 치킨집 고르기
	private static void getCombi(int cnt, int start, int[] combi) {
		if (cnt == m) {
			getDist(combi);
			return;
		}
		
		for (int i = start; i < chicken.size(); i++) {
			combi[cnt] = i;
			getCombi(cnt+1, i+1, combi);
		}
	}
	
	// 2. 최소 거리 구하기
	private static void getDist(int[] combi) {
		int distSum = 0;
		
		for (int i = 0; i < house.size(); i++) {
			int dist = Integer.MAX_VALUE;
			
			int hx = house.get(i)[0];
			int hy = house.get(i)[1];
			
			for (int j = 0; j < m; j++) {
				int cx = chicken.get(combi[j])[0];
				int cy = chicken.get(combi[j])[1];
				
				dist = Math.min(dist, Math.abs(hx-cx) + Math.abs(hy-cy));
			}
			
			distSum += dist;
		}

		answer = Math.min(answer, distSum);
	}

}
