import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		
		int[][] dxy = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
		
		int[][] arr = new int[n][m];
		StringTokenizer st;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < r; i++) {
			int[][] rotatedArr = new int[n][m];
			int sx = 0, sy = 0;	// 회전 영역의 시작 점
			int cx = 0, cy = 0;	// 원소가 이동하기 전의 위치
			int dir = 0;		// 방향 인덱스
			while (rotatedArr[sx][sy] == 0) {
				int nx = cx + dxy[dir][0], ny = cy + dxy[dir][1];	// 원소가 이동할 위치

				// 원소 이동
				if (nx < 0 || nx >= n || ny < 0 || ny >= m || rotatedArr[nx][ny] > 0) {
					dir = dir + 1 == 4 ? 1: dir + 1;
					nx = cx + dxy[dir][0];
					ny = cy + dxy[dir][1];
				}
				rotatedArr[nx][ny] = arr[cx][cy];
				
				cx = nx;
				cy = ny;
				if (cx == sx && cy == sy) {	// 안쪽으로 인덱스 이동
					cx ++;
					cy ++;
					sx ++;
					sy ++;
					dir = 0;
				}
			}
			
			arr = rotatedArr;	// 1번 회전 완료
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(arr[i][j] + " ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

}
