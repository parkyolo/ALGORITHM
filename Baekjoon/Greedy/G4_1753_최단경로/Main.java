package Baekjoon.Greedy.G4_1753_최단경로;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static class Node {
		int vertex, weight;
		Node next;
		
		public Node(int vertex, int weight, Node next) {
			this.vertex = vertex;
			this.weight = weight;
			this.next = next;
		}
		
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());	// 정점의 개수
		int E = Integer.parseInt(st.nextToken());	// 간선의 개수
		int K = Integer.parseInt(br.readLine());	// 시작 정점의 번호
		
		Node[] adjList = new Node[V+1];	// 인접 리스트
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjList[u] = new Node(v, w, adjList[u]);	// 유향 그래프
		}
		
		boolean[] visited = new boolean[V+1];
		int INF = Integer.MAX_VALUE;
		int[] distance = new int[V+1];
		Arrays.fill(distance, INF);
		distance[K] = 0;
		
		int minWeight = 0, minVertex = 0;
		
		for (int i = 0; i < V; i++) {
			minVertex = -1;
			minWeight = INF;
			for (int j = 1; j <= V; j++) {
				if (!visited[j] && distance[j] < minWeight) {
					minWeight = distance[j];
					minVertex = j;
				}
			}

			if (minVertex == -1) break;
			visited[minVertex] = true;	// 방문 체크
			
			for (Node temp = adjList[minVertex]; temp != null; temp = temp.next) {
				if (!visited[temp.vertex] && distance[temp.vertex] > minWeight + temp.weight) {
					distance[temp.vertex] = minWeight + temp.weight;
				}
			}
			
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= V; i++) {
			if (distance[i] == INF) sb.append("INF").append("\n");
			else sb.append(distance[i]).append("\n");
		}
		System.out.println(sb);
	}

}
