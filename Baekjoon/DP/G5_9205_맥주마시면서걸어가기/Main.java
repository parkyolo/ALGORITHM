/*
 * 1. summary
 * 상근이가 맥주 박스를 들고 집에서 페스티벌까지 가는데
 * 50m가 지나기 전에 맥주를 한 병씩 마신다.
 * 편의점에 들르면 새 맥주 병을 살 수 있다.
 * 박스의 맥주는 20병을 넘을 수 없다.
 * 
 * 2. strategy
 * 각 장소의 좌표를 저장하고 인덱스로 장소를 식별한다.(nodes[0]: 상근이 집,  nodes[n+1]: 페스티벌)
 * i에서 j까지의 맨해튼 거리를 구했을 때 1000 이하이면 이동할 수 있다.
 * 따라서 맨해튼 거리가 1000 이하인 장소 i,j(i!=j)에 대해 dist[i][j] = 1로 초기화한다.
 * 장소 간의 최단 거리를 구해서 집에서 페스티벌까지 이동할 수 있으면(dist[0][n+1]이 최대값보다 작으면) happy를 출력하고, 아니면 sad를 출력한다.
 * 
 * */

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int INF = 99999;
		
		for (int test_case = 0; test_case < t; test_case++) {
			int n = Integer.parseInt(br.readLine());	// 편의점의 개수
			
			Point[] nodes = new Point[n+2];		// 집, 편의점, 페스티벌의 좌표
			int[][] dist = new int[n+2][n+2];	// 좌표 간의 거리
			
			for (int i = 0; i < n+2; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				nodes[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			}	// 좌표 저장
			
			for (int i = 0; i < n+2; i++) {
				for (int j = 0; j < n+2; j++) {
					if (i == j) continue;
					if (Math.abs(nodes[i].x - nodes[j].x) + Math.abs(nodes[i].y - nodes[j].y) <= 1000) {
						dist[i][j] = 1;
					} else {
						dist[i][j] = INF;
					}
				}
			}	// 맥주 20병으로 이동할 수 있는 좌표를 1로 세팅
			
			for (int k = 0; k < n+2; k++) {
				for (int i = 0; i < n+2; i++) {
					for (int j = 0; j < n+2; j++) {
						if (i == j || j == k || k == i) continue;
						if (dist[i][j] > dist[i][k] + dist[k][j]) {
							dist[i][j] = dist[i][k] + dist[k][j];
						}
					}
				}
			}	// 좌표 간의 최단 거리 구하기

			// 0은 집, n+1은 페스티벌이므로 dist[0][n+1]의 값이 INF가 아니면 페스티벌에 도착할 수 있다.
			if (dist[0][n+1] == INF) System.out.println("sad");
			else System.out.println("happy");

		}
	}

}
