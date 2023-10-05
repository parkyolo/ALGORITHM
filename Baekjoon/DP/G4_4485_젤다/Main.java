package Baekjoon.DP.G4_4485_젤다;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

class Link implements Comparable<Link>{
	int x, y, cost;

	public Link(int x, int y, int cost) {
		this.x = x;
		this.y = y;
		this.cost = cost;
	}

	@Override
	public int compareTo(Link o) {
		return this.cost - o.cost;
	}
	
}

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		int INF = 125*125*10;
		int t = 0;
		
		while (true) {
			++t;
			int n = Integer.parseInt(br.readLine());
			if (n == 0) return;
			
			int[][] cave = new int[n][n];
			for (int i = 0; i < n; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					cave[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			Queue<Link> queue = new PriorityQueue<Link>();
			queue.offer(new Link(0, 0, cave[0][0]));
			
			int[][] dist = new int[n][n];
			for (int i = 0; i < dist.length; i++) Arrays.fill(dist[i], INF);
			dist[0][0] = cave[0][0];
			
			while (!queue.isEmpty()) {
				Link cur = queue.poll();
				if (cur.x == n-1 && cur.y == n-1) break;
				
				// 상하좌우 인접한 칸을 탐색하면서 더 적은 금액으로 이동할 수 있는 위치를 찾는다.
				for (int d = 0; d < 4; d++) {
					int nx = cur.x + dxy[d][0], ny = cur.y + dxy[d][1];
					if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
					
					int nv = cur.cost + cave[nx][ny];
					if (dist[nx][ny] <= nv) continue;
					
					dist[nx][ny] = nv;
					queue.offer(new Link(nx, ny, nv));
				}
			}
			
			System.out.println("Problem " + t + ": " + dist[n-1][n-1]);
		}
	}

}
