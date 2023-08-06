import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S3_11659_PrefixSum4 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int[] seq = new int[n+1];
		int[] prefix = new int[n+1];
		for (int i = 1; i < n+1; i++) {
			seq[i] = Integer.parseInt(st.nextToken());
			prefix[i] = prefix[i-1] + seq[i];
		}
		
		for (int k = 0; k < m; k++) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			
			System.out.println(prefix[j] - prefix[i-1]);
		}
	}

}
