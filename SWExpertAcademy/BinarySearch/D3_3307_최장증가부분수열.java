import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class D3_3307_최장증가부분수열 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= T; test_case++) {
			int n = Integer.parseInt(br.readLine());
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			int arr[] = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			int[] lis = new int[n];
			int end = 0;
			for (int i = 0; i < n; i++) {
				int insPosition = Arrays.binarySearch(lis, 0, end, arr[i]);
				
				insPosition = Math.abs(insPosition) - 1;
				lis[insPosition] = arr[i];
				
				if (end == insPosition) end++;
			}
			
			System.out.println("#" + test_case + " " + end);
		}
	}

}
