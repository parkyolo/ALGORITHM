import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		int[] memo = new int[12];
		memo[1] = 1;
		memo[2] = 2;
		memo[3] = 4;
		
		for (int i = 4; i < 12; i++) {
			memo[i] = memo[i-3] + memo[i-2] + memo[i-1];
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < t; i++) {
			int n = Integer.parseInt(br.readLine());
			sb.append(memo[n]).append("\n");
		}
		System.out.println(sb);
	}

}
