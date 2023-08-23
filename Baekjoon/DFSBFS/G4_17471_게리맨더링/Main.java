/*
 * 1. summary
 * 1번부터 N번까지의 구역을 두 개로 나눠 인구 수 차이가 최소가 되도록 한다.
 * 인구 수 차이의 최솟값을 출력한다.
 * 
 * 2. strategy
 * 부분 집합을 통해 1부터 N을 두 개의 집합으로 나눈다.
 * 두 집합에 속한 정점들의 인구 수 합을 구한다.
 * 정점이 모두 연결되어 있지 않으면 다음 집합을 검사한다.
 * 인구 수 차이의 최솟값을 갱신한다.
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	
	static int n, popul[], graph[][], minDiff;
	static boolean isSelected[];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		popul = new int[n+1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= n; i++) {
			popul[i] = Integer.parseInt(st.nextToken());
		}
		
		graph = new int[n+1][];

		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			int len = Integer.parseInt(st.nextToken());
			graph[i] = new int[len];
			for (int j = 0; j < len; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		isSelected = new boolean[n+1];
		minDiff = -1;
		getSubSet(1, 0);
		System.out.println(minDiff);
	}
	
	// 부분 집합 구하기
	private static void getSubSet(int cnt, int selectedCount) {
		if (cnt == n) {
			if (selectedCount > 0) {
				check(selectedCount);
			}
			return;
		}
		
		isSelected[cnt] = true;
		getSubSet(cnt+1, selectedCount+1);
		isSelected[cnt] = false;
		getSubSet(cnt+1, selectedCount);
	}

	private static void check(int len) {
		Set<Integer> area1 = new HashSet<Integer>();
		Set<Integer> area2 = new HashSet<Integer>();
		
		// 1부터 N을 두 개의 집합으로 나눔
		// 집합의 시작 정점 번호를 저장
		int start1 = 0, start2 = 0;
		for (int i = 1; i <= n; i++) {
			if (isSelected[i]) {
				area1.add(i);
				if (start1 == 0) start1 = i;
			}
			else {
				area2.add(i);
				if (start2 == 0) start2 = i;
			}
		}
		
		// 두 구역의 인구 수
		// 구역이 서로 연결되어 있지 않으면 -1이 return 반환된다.
		int cnt1, cnt2;
		if ((cnt1 = bfs(area1, start1)) == -1) return;
		if ((cnt2 = bfs(area2, start2)) == -1) return;
		
		// 인구 수 차이의 최솟값 갱신
		int diff = Math.abs(cnt1 - cnt2);
		if (minDiff == -1) {	// 최솟값 초기화
			minDiff = diff;
			return;
		}
		minDiff = Math.min(minDiff, diff);
	}
	
	private static int bfs(Set<Integer> area, int start) {
		boolean visited[] = new boolean[n+1];
		Queue<Integer> queue = new ArrayDeque<>();
		queue.offer(start);
		visited[start] = true;
		
		int cnt = 0;	// 방문 도시 수
		int pcnt = 0;	// 인구 수
		while (!queue.isEmpty()) {
			int current = queue.poll();
			cnt++;
			pcnt += popul[current];
			for (Integer next : graph[current]) {
				if (visited[next]) continue;
				if (!area.contains(next)) continue;
				visited[next] = true;
				queue.offer(next);
			}
		}
		
		if (cnt == area.size()) return pcnt;
		return -1;	// 모든 도시를 방문할 수 없을 때
	}

}
