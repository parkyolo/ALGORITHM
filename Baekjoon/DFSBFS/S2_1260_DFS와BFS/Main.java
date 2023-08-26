package Baekjoon.DFSBFS.S2_1260_DFS와BFS;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	private static int n, adjMatrix[][];
	private static boolean visited[];
	private static StringBuilder sb;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());	    // 정점의 개수
		int m = Integer.parseInt(st.nextToken());	// 간선의 개수
		int v = Integer.parseInt(st.nextToken());	// 탐색을 시작할 정점 번호
		
		adjMatrix = new int[n+1][n+1];
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			adjMatrix[a][b] = 1;
			adjMatrix[b][a] = 1;
		}
		
		visited = new boolean[n+1];
		visited[v] = true;
		sb = new StringBuilder();
		dfs(v);
		System.out.println(sb);
		
		visited = new boolean[n+1];
		visited[v] = true;
		sb = new StringBuilder();
		bfs(v);
		System.out.println(sb);
	}

	private static void dfs(int v) {
		sb.append(v + " ");
		for (int i = 1; i <= n; i++) {
			if (adjMatrix[v][i] == 1 && !visited[i]) {
				visited[i] = true;
				dfs(i);
			}
		}
	}

	private static void bfs(int v) {
		Queue<Integer> queue = new ArrayDeque<>();
		queue.offer(v);
		
		while (!queue.isEmpty()) {
			int current = queue.poll();
			sb.append(current + " ");
			for (int i = 1; i <= n; i++) {
				if (adjMatrix[current][i] == 1 && !visited[i]) {
					visited[i] = true;
					queue.offer(i);
				}
			}
		}
	}
}
