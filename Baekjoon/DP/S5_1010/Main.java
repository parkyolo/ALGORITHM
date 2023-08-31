import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int n = 30;
		int m = 30;
		int dp[][] = new int[n+1][m+1];
			for (int j = 1; j <= m; j++) {
				dp[1][j] = j;
			}
			
			for (int j = 2; j <= n; j++) {
				for (int k = 1; k <= m; k++) {
					dp[j][k] = dp[j-1][k-1] + dp[j][k-1];
				}
			}
			
		for (int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			
			System.out.println(dp[n][m]);
		}
	}

}
