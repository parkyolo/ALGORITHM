import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

class Move {
	int x, y, cnt, key;

	public Move(int x, int y, int cnt, int key) {
		this.x = x;
		this.y = y;
		this.cnt = cnt;
		this.key = key;
	}
	
}

public class G1_달이차오른다가자 {
	
	public static void main(String[] args) throws Exception {
		
		int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		Set<Character> door = new HashSet<>();
		Set<Character> keys = new HashSet<>();
		
		door.add('A');
		door.add('B');
		door.add('C');
		door.add('D');
		door.add('E');
		door.add('F');
		
		keys.add('a');
		keys.add('b');
		keys.add('c');
		keys.add('d');
		keys.add('e');
		keys.add('f');		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int sx = 0, sy = 0;	// 민식이 출발 위치
		
		char[][] maze = new char[n][m];
		for (int i = 0; i < n; i++) {
			String row = br.readLine();
			for (int j = 0; j < m; j++) {
				maze[i][j] = row.charAt(j);
				if (maze[i][j] == '0') {
					sx = i;
					sy = j;
				}
			}
		}
		
		boolean visited[][][] = new boolean[n][m][1<<'g'];
		Queue<Move> queue = new ArrayDeque<>();
		queue.offer(new Move(sx, sy, 0, 1));
		visited[sx][sy][1] = true;
		
		while (!queue.isEmpty()) {
			Move cur = queue.poll();
			int cx = cur.x;
			int cy = cur.y;
			
			if (maze[cx][cy] == '1') {
				System.out.println(cur.cnt);
				return;
			}
			
			for (int d = 0; d < 4; d++) {
				int nx = cx + dxy[d][0], ny = cy + dxy[d][1];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;	// 범위를 벗어나는 경우
				if (maze[nx][ny] == '#') continue;	// 벽인 경우
				if (door.contains(maze[nx][ny]) && ((cur.key & (1<<maze[nx][ny])) == 0)) continue;	// 문인데 열쇠가 없는 경우
				if (visited[nx][ny][cur.key]) continue;	// 이미 방문한 경우
				
				int nk = cur.key;
				if (keys.contains(maze[nx][ny])) {	// 열쇠가 있는 위치인 경우
					nk = cur.key | (1<<maze[nx][ny]);
				}
				visited[nx][ny][nk] = true;
				queue.offer(new Move(nx, ny, cur.cnt+1, nk));
			}
		}
		
		System.out.println(-1);
	}

}
