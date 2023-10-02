import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static class Monkey {
		int x, y, jump, cnt;

		public Monkey(int x, int y, int jump, int cnt) {
			super();
			this.x = x;
			this.y = y;
			this.jump = jump;
			this.cnt = cnt;
		}
		
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int w = Integer.parseInt(st.nextToken());
		int h = Integer.parseInt(st.nextToken());
		
		int map[][] = new int[h][w];
		for (int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < w; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());

			}
		}
		
		int dxy[][] = {
				{-1, 0}, {1, 0}, {0, -1}, {0, 1},
				{-2, -1}, {-1, -2}, {-2, 1}, {-1, 2},
				{2, -1}, {1, -2}, {2, 1}, {1, 2}
		};
		
		Queue<Monkey> queue = new ArrayDeque<>();
		queue.offer(new Monkey(0, 0, 0, 0));
		
		int visited[][][] = new int[h][w][k+1];
		int answer = -1;
		
		while (!queue.isEmpty()) {
			Monkey monkey = queue.poll();
			
			if (monkey.x == h-1 && monkey.y == w-1) {
				answer = monkey.cnt;
				break;
			}
			
			for (int d = 0; d < 12; d++) {
				int nx = monkey.x + dxy[d][0], ny = monkey.y + dxy[d][1];
				if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
				if (map[nx][ny] == 1) continue;
				
				if (d < 4) {
					if (visited[nx][ny][monkey.jump] != 0 && visited[nx][ny][monkey.jump] <= monkey.cnt+1) continue;
					queue.offer(new Monkey(nx, ny, monkey.jump, monkey.cnt+1));
					visited[nx][ny][monkey.jump] = monkey.cnt+1;
					continue;
				}
				
				if (monkey.jump < k) {
					if (visited[nx][ny][monkey.jump+1] != 0 && visited[nx][ny][monkey.jump+1] <= monkey.cnt+1) continue;
					queue.offer(new Monkey(nx, ny, monkey.jump+1, monkey.cnt+1));
					visited[nx][ny][monkey.jump+1] = monkey.cnt+1;
				}
			}
		}

		System.out.println(answer);
	}

}
