package SWExpertAcademy.DataStructures;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D4_3289_DisjointSet {
	
	private static int parents[];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			parents = new int[n+1];
			for (int i = 1; i <= n; i++) {
				parents[i] = i;
			}
			
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(test_case).append(" ");
			
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int flag = Integer.parseInt(st.nextToken());	// 0이면 합집합, 1이면 확인
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				if (flag == 0) {
					union(a, b);
				} else if (flag == 1) {
					int rootA = find(a);
					int rootB = find(b);
					
					if (rootA == rootB) sb.append(1);
					else if (rootA != rootB) sb.append(0);
				}
			}
			
			System.out.println(sb);
		}
	}

	private static void union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		
		if (rootA == rootB) return;
		if (a < b) parents[rootB] = rootA;
		else parents[rootA] = rootB;
	}

	private static int find(int a) {
		if (parents[a] == a) return a;
		return parents[a] = find(parents[a]);
	}

}
