/*
 * 1. summary
 * 가로 파이프는 가로, 대각선 방향, 세로 파이프는 세로, 대각선 방향, 대각선 파이프는 가로, 세로, 대각선 방향으로 밀 수 있다.
 * N*N 격자판 끝으로 파이프를 이동시키는 방법의 수를 구한다.
 * 
 * 2. strategy
 * (i,j)위치에 가로, 세로, 대각선으로 파이프를 이동시키는 방법의 수를 저장한다.
 * (i,j)에 파이프가 가로 방향으로 놓이려면 왼쪽 칸에 가로나 대각선에서 이동시킬 수 있다.
 * 				세로 방향으로 놓이려면 위쪽 칸에 세로나 대각선에서 이동시킬 수 있다.
 * 				대각선으로 놓이려면 위쪽과 왼쪽이 빈칸이어야 하고, 가로, 세로, 대각선에서 이동시킬 수 있다.
 * (n,n)위치의 가로, 세로, 대각선을 더해서 출력한다.
 * 
 * */
 
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int state[][] = new int[n+1][n+1];
		StringTokenizer st;
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				state[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int dp[][][] = new int[n+1][n+1][3];	// 가로, 세로, 대각선으로 놓일 수 있는 횟수
		dp[1][2][0] = 1;
		
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (state[i][j] == 1) continue;
				dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2];
				dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2];
				if (state[i-1][j] == 1 || state[i][j-1] == 1) continue;
				dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
			}
		}
		
		System.out.println(dp[n][n][0] + dp[n][n][1] + dp[n][n][2]);
	}

}
