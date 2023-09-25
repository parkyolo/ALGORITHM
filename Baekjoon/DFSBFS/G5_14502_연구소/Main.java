import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m, map[][], blank, maxArea, wall = 3;
	static ArrayList<Point> coord;
	static int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	static int[] combi;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		// coord[i]: n*m개의 칸 중 i번째 칸의 좌표
		coord = new ArrayList<Point>();
		// 0은 빈 칸, 1은 벽, 2는 바이러스
		map = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 0) {	// 빈 칸(벽을 세울 수 있는 공간)의 좌표 저장
					coord.add(new Point(i, j));
				}
			}
		}
		
		blank = coord.size();	// 빈 칸의 개수
		maxArea = 0;			// 안전 영역 크기의 최댓값
		combi = new int[wall];	// 벽 세울 곳 조합
		
		
		// 벽 3개 세우기
		getCombi(0, 0);
		
		System.out.println(maxArea);
	}
	
	public static void getCombi(int cnt, int start) {
		if (cnt == wall) {
			getArea();
			return;
		}
		
		for (int i = start; i < blank; i++) {
			combi[cnt] = i;
			getCombi(cnt+1, i+1);
		}
	}
	
	public static void getArea() {
		// 벽 세우기
		for (int c : combi) {
			map[coord.get(c).x][coord.get(c).y] = 1;
		}
		
		// 바이러스 퍼트리기
		boolean visited[][] = new boolean[n][m];	// 바이러스가 지나간 곳 체크
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] != 2) continue;	// 바이러스이면 확산 시작
				Queue<Point> queue = new ArrayDeque<Point>();
				queue.offer(new Point(i, j));
				visited[i][j] = true;
				while (!queue.isEmpty()) {
					Point p = queue.poll();
					int cx = p.x, cy = p.y;
					for (int d = 0; d < 4; d++) {
						int nx = cx + dxy[d][0], ny = cy + dxy[d][1];
						if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;	// 범위 체크
						if (visited[nx][ny]) continue;	// 방문 체크
						if (map[nx][ny] != 0) continue;	// 빈칸일 때만 확산
						visited[nx][ny] = true;
						queue.offer(new Point(nx, ny));
					}
				}
			}
		}
		
		// 안전 영역 크기 구하기
		int safeArea = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0 && !visited[i][j]) safeArea++;
			}
		}
		
		maxArea = Math.max(maxArea, safeArea);
		
		// 벽 초기화
		for (int c : combi) {
			map[coord.get(c).x][coord.get(c).y] = 0;
		}
	}

}
