package Baekjoon.DFSBFS.G1_17472_다리만들기2;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
	int from, to, weight;

	public Edge(int from, int to, int weight) {
		this.from = from;
		this.to = to;
		this.weight = weight;
	}

	@Override
	public int compareTo(Edge o) {
		return this.weight - o.weight;
	}
}

public class Main {
    static int[] parents;
	
	public static void main(String[] args) throws Exception {
		
		int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int INF = n*m;

		int map[][] = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 섬을 숫자로 구분한다.
		int islandNum = 0;
		boolean visited[][] = new boolean[n][m];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					Queue<Point> queue = new ArrayDeque<Point>();
					queue.offer(new Point(i, j));
					visited[i][j] = true;
					map[i][j] = ++islandNum;
					while (!queue.isEmpty()) {
						Point cur = queue.poll();
						
						for (int d = 0; d < 4; d++) {
							int nx = cur.x + dxy[d][0], ny = cur.y + dxy[d][1];
							if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
							if (map[nx][ny] == 0) continue;
							if (visited[nx][ny]) continue;
							queue.offer(new Point(nx, ny));
							visited[nx][ny] = true;
							map[nx][ny] = islandNum;
						}
					}
				}
			}
		}
		
		int dist[][] = new int[islandNum+1][islandNum+1];
		for (int k = 0; k < islandNum+1; k++) {	// 현재 섬에서 다른 섬까지의 거리를 최대값으로 초기화
			Arrays.fill(dist[k], INF);
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0) continue;
				int curNum = map[i][j];	// 현재 섬의 번호
				
				// 가로, 세로로 이을 수 있는 다른 섬 찾기
				for (int d = 0; d < 4; d++) {
					int x = i + dxy[d][0], y = j + dxy[d][1];
					while ((x >= 0 && x < n && y >= 0 && y < m) && map[x][y] == 0) {
						x += dxy[d][0];
						y += dxy[d][1];
					}
					if (x < 0 || x >= n || y < 0 || y >= m) continue;
					
					if (map[x][y] != curNum) {	// 다른 섬과 이어졌다면
						int distance = Math.abs(i-x) + Math.abs(j-y) - 1;
						int otherNum = map[x][y];
						if (distance > 1) {	// 거리가 2 이상이면 최솟값으로 갱신
							dist[curNum][otherNum] = Math.min(dist[curNum][otherNum], distance);
							dist[otherNum][curNum] = Math.min(dist[curNum][otherNum], distance);
						}
					}
				}
			}
		}
		
		// 섬의 번호로 유니온파인드
		parents = new int[islandNum+1];
		for (int i = 0; i < islandNum+1; i++) {
			parents[i] = i;
		}
		
		// 섬 간의 거리가 짧은 순으로 우선순위큐에 넣음
		Queue<Edge> pq = new PriorityQueue<Edge>();
		for (int i = 1; i < islandNum+1; i++) {
			for (int j = 1; j < islandNum+1; j++) {
				if (dist[i][j] < INF) pq.offer(new Edge(i, j, dist[i][j]));
			}
		}
		
		int minDist = 0;	// 모든 섬을 연결하는 다리 길이의 최솟값
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();
			if (!union(cur.from, cur.to)) continue;
			minDist += cur.weight;
		}
		
		boolean flag = true;	// 모든 섬이 연결되지 않았으면 false
		for (int i = 1; i < islandNum; i++) {
			if (find(i) != find(i+1)) flag = false;
		}
		if (flag) System.out.println(minDist);
		else System.out.println(-1);
		
		
	}
	
	private static int find(int a) {
		if (parents[a] == a) return a;
		return parents[a] = find(parents[a]);
	}

	private static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		
		if (aRoot == bRoot) return false;

		if (a < b) parents[bRoot] = aRoot;
		else parents[aRoot] = bRoot;
		return true;
	}

}
