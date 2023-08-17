/*
 * 1. summary
 * 10*10 영역의 지도에 BC(Battery Charger)가 A개 설치되어 있다.
 * BC는 충전 범위 C 이내에 들어오면 충전이 가능하다.
 * A와 B가 (0,0), (9,9)에서 출발한 이동 궤적이 주어진다.
 * A와 B가 같은 BC를 사용했을 때 충전량을 분배해야 하므로 다른 BC에 접속하는 것이 더 이득이다.
 * A와 B의 충전량의 최댓값을 구한다.
 * 
 * 2. strategy
 * - BC의 충전 범위는 C만큼 상하좌우로 뻗어나간다. C를 1씩 감소하면서 충전범위를 배열에 체크한다.
 * - (r,c)에서 접속할 수 있는 BC는 map[r][c]에 충전량의 내림차순으로 저장한다.
 * - A와 B를 이동하며 해당 위치에 BC가 있는지 검사한다.
 * 	- 서로 다른 BC가 있다면 모두 충전량 amount에 더해준다.
 * 	- 같은 BC가 있다면, 사용할 수 있는 다른 BC가 있는지 검사한다.
 * - A와 B의 위치에 있는 BC를 모두 충전량으로 내림차순되는 우선순위 큐 temp에 저장하고
 *   temp의 원소가 1개일 경우 1개만, 2개 이상일 경우 2개를 amount에 더해준다.
 *   
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 5644_WirelessCharging {
	
	static class Pair implements Comparable<Pair> {	// BC의 power와 index를 담을 class
		int power;
		int idx;
		
		public Pair(int power, int idx) {
			this.power = power;
			this.idx = idx;
		}
		
		@Override
		public int compareTo(Pair o) {	// power의 내림차순으로 정렬
			return o.power - this.power;
		}
		
		
	}
	
	private static PriorityQueue<Pair>[][] map;
	private static int[][] dxy = {{0, 0}, {-1, 0}, {0, 1}, {1, 0}, {0, -1}};

	public static void main(String[] args) throws Exception {
		BufferedReader br_ = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br_.readLine());
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br_.readLine());
			int m = Integer.parseInt(st.nextToken());	// 이동 시간
			int a = Integer.parseInt(st.nextToken());	// BC의 개수
			
			int[] moveA = new int[m];	// A의 이동 정보
			int[] moveB = new int[m];	// B의 이동 정보
			
			st = new StringTokenizer(br_.readLine());
			for (int i = 0; i < m; i++) {
				moveA[i] = Integer.parseInt(st.nextToken());
			}
			
			st = new StringTokenizer(br_.readLine());
			for (int i = 0; i < m; i++) {
				moveB[i] = Integer.parseInt(st.nextToken());
			}
			
			map = new PriorityQueue[10][10];	// BC의 충전 범위
			for (int i = 0; i < a; i++) {
				st = new StringTokenizer(br_.readLine());
				int y = Integer.parseInt(st.nextToken());
				int x = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				int p = Integer.parseInt(st.nextToken());
				x--;
				y--;
				if (map[x][y] == null) {
					map[x][y] = new PriorityQueue<>();
				}
				map[x][y].add(new Pair(p, i));
				getArea(x, y, c, p, i);	// BC가 충전 가능한 범위 설정
			}

			int amount = 0;		// 총 충전량
			int ar = 0, ac = 0;	// A의 출발 위치
			int br = 9, bc = 9;	// B의 출발 위치
			
			for (int i = 0; i <= m; i++) {	// 출발 위치부터 충전가능한지 검사
				int ai = -1, bi = -1;		// A와 B가 사용할 BC의 index
				if (map[ar][ac] != null) {
					ai = map[ar][ac].peek().idx;
				}
				if (map[br][bc] != null) {
					bi = map[br][bc].peek().idx;
				}
				
				if (ai != bi) {	// BC가 서로 다르면 바로 충전
					if (ai != -1) {
						amount += map[ar][ac].peek().power;
					}
					if (bi != -1) {
						amount += map[br][bc].peek().power;
					}
				}
				if (ai != -1 && ai == bi) {	// BC가 같으면 어떤 충전기를 사용할지 정해줘야 함
					boolean isSelected[] = new boolean[a];
					// 사용 가능한 충전기의 power가 내림차순 정렬되어 있는 우선순위 큐
					PriorityQueue<Integer> temp = new PriorityQueue<Integer>(Collections.reverseOrder());
					
					// 사용 가능한 충전기를 모두 temp에 넣음
					for (Pair pair : map[ar][ac]) {
						if (!isSelected[pair.idx]) {
							temp.add(pair.power);
							isSelected[pair.idx] = true;
						}
					}
					for (Pair pair : map[br][bc]) {
						if (!isSelected[pair.idx]) {
							temp.add(pair.power);
							isSelected[pair.idx] = true;
						}
					}
					
					amount += temp.poll();
					// 서로 다른 충전기를 사용할 수 있으면 다른 충전기 사용
					if (temp.size() > 0) amount += temp.poll();
				}
				
				// m번째일 땐 다음 위치가 없으므로 break
				if (i == m) break;
				
				// 다음 위치로 이동
				ar += dxy[moveA[i]][0];
				ac += dxy[moveA[i]][1];
				br += dxy[moveB[i]][0];
				bc += dxy[moveB[i]][1];
			}
			
			System.out.println("#" + test_case + " " + amount);
			
		}
	}
	
	private static void getArea(int x, int y, int c, int p, int index) {	// 충전 범위 설정
		if (c == 0) return;	// c만큼의 영역에서 충전 가능
		
		for (int i = 1; i <= 4; i++) {	// 현재 위치를 기준으로 4방향으로 뻗어나감
			int nx = x + dxy[i][0], ny = y + dxy[i][1];
			if (nx < 0 || nx >= 10 || ny < 0 || ny >= 10) continue;
			boolean flag = true;
			if (map[nx][ny] != null) {	// 같은 BC가 두 번 추가되지 않도록 검사
				for (Pair pair : map[nx][ny]) {
					if (pair.idx == index) {
						flag = false;
						break;
					}
				}
			}
			if (map[nx][ny] == null) {
				map[nx][ny] = new PriorityQueue<>();
			}
			if (flag) {
				map[nx][ny].add(new Pair(p, index));
			}

			getArea(nx, ny, c-1, p, index);
			
		}
	}

}
