import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class S2_2961_DeliciousFood {
	
	private static int n, ingredient[][], diff;
	private static boolean[] set;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		ingredient = new int[n][];
		for (int i = 0; i < n; i++) {
			ingredient[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		
		diff = Math.abs(ingredient[0][1] - ingredient[0][0]);
		set = new boolean[n];
		
		getCombi(0, 0, 1, 0);
		System.out.println(diff);
	}
	
	public static void getCombi(int idx, int selectedCount, int sour, int bitter) {
		if (idx == n) {
			if (selectedCount > 0) {
				if (Math.abs(sour-bitter) < diff) {
					diff = Math.abs(sour-bitter);
				}
			}
			return;
		}
		set[idx] = true;
		getCombi(idx+1, selectedCount+1, sour*ingredient[idx][0], bitter+ingredient[idx][1]);
		set[idx] = false;
		getCombi(idx+1, selectedCount, sour, bitter);
	}

}
