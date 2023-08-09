/*
 * 1. summary
 * N*N 배열에 서로 다른 숫자가 적혀있다.
 * 한 좌표에서 상하좌우로 인접한 칸에 현재보다 1만큼 큰 숫자가 적혀있으면 이동할 수 있다.
 * 처음에 어떤 숫자가 적힌 방에서 출발해야 가장 많은 방을 이동할 수 있는지 구한다.
 * 
 * 2. strategy
 * N*N 배열의 모든 좌표에 대해 상하좌우 인접한 칸을 탐색하는 bfs 메소드를 실행한다.
 * 현재보다 1만큼 큰 숫자가 적힌 인접 칸에 대해 cnt를 증가시키며 bfs를 실행하고 가장 큰 이동횟수를 반환한다.
 * 출발하는 칸의 숫자와 최대 이동횟수를 출력한다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Pair {
	int x;
	int y;
	int cnt;
	
	Pair(int y, int x, int cnt) {
		this.y = y;
		this.x = x;
		this.cnt = cnt;
	}
}

public class D4_1861_SquareRoom {

	private static int n;
	private static int[][] room;
	private static int[][] dxy = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= t; test_case++) {
			n = Integer.parseInt(br.readLine());
			room = new int[n][n];
			StringTokenizer st;
			for (int j = 0; j < n; j++) {
				st = new StringTokenizer(br.readLine());
				for (int i = 0; i < n; i++) {
					room[j][i] = Integer.parseInt(st.nextToken());
				}
			}
			
			int maxCnt = 0;	// 최대 이동 횟수
			int ansY = 0, ansX = 0;
			
			int moveCnt;
			for (int j = 0; j < n; j++) {
				for (int i = 0; i < n; i++) {
					moveCnt = bfs(j, i);
					if (moveCnt > maxCnt) {
						maxCnt = moveCnt;
						ansY = j;
						ansX = i;
					} else if (moveCnt == maxCnt) {
						if (room[ansY][ansX] > room[j][i]) {
							ansY = j;
							ansX = i;
						}
					}
				}
			}
			
			System.out.println("#" + test_case + " " + room[ansY][ansX] + " " + maxCnt);
		}
	}

	public static int bfs(int y, int x) {
		int moveCnt = 0;
		Queue<Pair> queue = new LinkedList<>();
		queue.offer(new Pair(y, x, 1));
		
		while (!queue.isEmpty()) {
			Pair cur = queue.poll();
			moveCnt = Math.max(moveCnt, cur.cnt);
			for (int i = 0; i < 4; i++) {
				int ny = cur.y + dxy[i][0], nx = cur.x + dxy[i][1];
				if (ny < 0 || ny >= n || nx < 0 || nx >= n) continue;
				if (room[ny][nx] != room[cur.y][cur.x] + 1) continue;
				queue.offer(new Pair(ny, nx, cur.cnt+1));
			}
		}
		
		return moveCnt;
	}
}
