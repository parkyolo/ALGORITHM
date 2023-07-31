import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws Exception {
		int n = 19;
		int[][] dxy = {{-1, 1}, {0, 1}, {1, 1}, {1, 0}};
		int[][] board = new int[n][n];
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
				
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (board[i][j] == 1 || board[i][j] == 2) {
					int[][] visited = new int[n][n];
					int num = board[i][j];
					visited[i][j] = 0;
					for (int k = 0; k < 4; k++) {
						int cnt = 1;
						int ci = i, cj = j;
						while (cnt <= 6) {
							int ni = ci + dxy[k][0], nj = cj + dxy[k][1];
							if (ni < 0 || ni >= n || nj < 0 || nj >= n) break;
							if (board[ni][nj] != num) break;
							if (visited[ni][nj] == 1) break;
							cnt ++;
							visited[ni][nj] = 1;
							ci = ni;
							cj = nj;
						}
						if (cnt == 5) {
							int ni = i + (-1) * dxy[k][0], nj = j + (-1) * dxy[k][1];
							if (!(ni < 0 || ni >= n || nj < 0 || nj >= n) && board[ni][nj] == num) continue;
							System.out.println(num);
							System.out.println((i+1) + " " + (j+1));
							return;
						}
					}
					
				}
			}
		}
		System.out.println("0");
		
	}
}