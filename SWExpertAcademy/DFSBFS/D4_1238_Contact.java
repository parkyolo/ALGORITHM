/*
 * 1. summary
 * 유향 그래프의 간선 정보가 주어졌을 때 시작 정점과 가장 먼 정점 중 숫자가 가장 큰 정점을 구한다.
 * 
 * 2. strategy
 * 너비 우선 탐색을 통해 가장 먼 정점을 구한다.
 * 
 * */

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class D4_1238_Contact {
	
	static int MAXINT = 100;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = 10;
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int len = Integer.parseInt(st.nextToken());		// 입력받는 데이터 길이
			int start = Integer.parseInt(st.nextToken());	// 연락을 시작하는 당번
			
			List<Integer>[] graph = new ArrayList[MAXINT+1];
			for (int i = 0; i <= MAXINT; i++) {
				graph[i] = new ArrayList<Integer>();
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < len/2; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				
				graph[from].add(to);
			}
			
			int maxDist = 0;	// 최대 거리
			int answer = 0;		// 마지막에 연락을 받을 사람(시작 정점과 가장 먼 정점)
			
			// 방문 체크
			boolean[] visited = new boolean[MAXINT+1];
			visited[start] = true;	
			
			Queue<Point> queue = new ArrayDeque<>();
			queue.offer(new Point(start, 0));	// x: 노드 번호, y: 거리
			
			while (!queue.isEmpty()) {
				Point current = queue.poll();
				
				if (current.y > maxDist) {
					maxDist = current.y;
					answer = current.x;
				} else if (current.y == maxDist) {	// 마지막에 연락을 받은 사람이 여러 명이면 숫자가 큰 사람
					answer = Math.max(answer, current.x);
				}
				
				for (Integer next : graph[current.x]) {
					if (visited[next]) continue;
					visited[next] = true;
					queue.offer(new Point(next, current.y+1));
				}
			}
			
			System.out.println("#" + test_case + " " + answer);
		}
	}

}
