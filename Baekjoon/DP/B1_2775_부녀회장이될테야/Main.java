import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		int memo[][] = new int[15][15];
		for (int i = 0; i < 15; i++) {
			memo[0][i] = i;
		}
		
		for (int i = 1; i < 15; i++) {
			for (int j = 1; j < 15; j++) {
				memo[i][j] = memo[i][j-1] + memo[i-1][j];
			}
			
		}
		
		for (int test_case = 0; test_case < t; test_case++) {
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
			
			System.out.println(memo[k][n]);
		}
	}

}
