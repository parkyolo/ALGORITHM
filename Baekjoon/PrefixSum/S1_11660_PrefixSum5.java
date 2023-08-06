import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S1_11660_PrefixSum5 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		
		int[][] seq = new int[n+1][n+1];
		int[][] prefix = new int[n+1][n+1];
		for (int j = 1; j < n+1; j++) {
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i < n+1; i++) {
				seq[j][i] = Integer.parseInt(st.nextToken());
				prefix[j][i] = prefix[j][i-1] + prefix[j-1][i] - prefix[j-1][i-1] + seq[j][i];
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int k = 0; k < m; k++) {
			
			st = new StringTokenizer(br.readLine());
			int y1 = Integer.parseInt(st.nextToken());
			int x1 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			
			sb.append(prefix[y2][x2] - prefix[y1-1][x2] - prefix[y2][x1-1] + prefix[y1-1][x1-1] + "\n");
		}
		System.out.println(sb);
	}

}
