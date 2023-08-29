import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int memo[] = new int[n+1];
		memo[0] = 1;
		memo[1] = 1;
		
		for (int i = 2; i <= n; i++) {
			memo[i] = (memo[i-1] + memo[i-2]) % 10007;
		}
		
		System.out.println(memo[n]);
	}

}
