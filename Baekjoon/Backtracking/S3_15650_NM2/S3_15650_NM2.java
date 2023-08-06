import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S3_15650_NM2 {
	
	private static int n, m;
	private static int[] seq;
	private static boolean[] isSelected;

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		n = Integer.parseInt(input.split(" ")[0]);
		m = Integer.parseInt(input.split(" ")[1]);
		seq = new int[m];
		isSelected = new boolean[n+1];
		getSeq(0, 1);
	}
	
	private static void getSeq(int idx, int start) {
		if (idx == m) {
			for (int i = 0; i < m; i++) {
				System.out.print(seq[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = start; i <= n; i++) {
			if (isSelected[i]) continue;
			isSelected[i] = true;
			seq[idx] = i;
			getSeq(idx+1, i+1);
			isSelected[i] = false;
		}
	}

}
