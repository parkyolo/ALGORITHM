import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int cost[][] = new int[n][3];
		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				cost[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 1; i < n; i++) {
			for (int j = 0; j < 3; j++) {
				cost[i][j] += Math.min(cost[i-1][(j+2)%3], cost[i-1][(j+1)%3]);
			}
		}
		
		int answer = Integer.MAX_VALUE;
		for (int j = 0; j < 3; j++) {
			answer = Math.min(answer, cost[n-1][j]);
		}
		System.out.println(answer);
	}

}
