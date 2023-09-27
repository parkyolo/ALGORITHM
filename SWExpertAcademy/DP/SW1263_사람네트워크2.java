import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SW1263_사람네트워크2 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int INF = 99999;
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int[][] dist = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					dist[i][j] = Integer.parseInt(st.nextToken());
					if (i != j && dist[i][j] == 0) {
						dist[i][j] = INF;
					}
				}
			}
			
			for (int k = 0; k < n; k++) {
				for (int i = 0; i < n; i++) {
					if (k == i) continue;
					
					for (int j = 0; j < n; j++) {
						if (i == j || k == j) continue;
						if (dist[i][j] > dist[i][k] + dist[k][j])
							dist[i][j] = dist[i][k] + dist[k][j];
					}
					
				}
			}
			
			int cc = INF;
			for (int i = 0; i < n; i++) {
				int distsum = 0;
				for (int j = 0; j < n; j++) {
					if (dist[i][j] != INF) distsum += dist[i][j];
				}
				if (distsum < cc) {
					cc = distsum;
				}
			}
			
			System.out.println("#" + test_case + " " + cc);
		}
		
		
	}

}
