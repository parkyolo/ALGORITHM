package SWExpertAcademy.Implementation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Tank {
	int r, c, dir;

	public Tank(int r, int c, int dir) {
		super();
		this.r = r;
		this.c = c;
		this.dir = dir;
	}
	
}

public class D3_1873_BattleField {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int h = Integer.parseInt(st.nextToken());	// 게임 맵의 높이
			int w = Integer.parseInt(st.nextToken());	// 게임 맵의 너비
			
			Tank tank = new Tank(0, 0, 0);
			
			char[][] map = new char[h][w];
			for (int i = 0; i < h; i++) {
				String line = br.readLine();
				for (int j = 0; j < w; j++) {
					map[i][j] = line.charAt(j);
					if (map[i][j] == '^') {
						tank = new Tank(i, j, 0);
					} else if (map[i][j] == 'v') {
						tank = new Tank(i, j, 1);
					} else if (map[i][j] == '<') {
						tank = new Tank(i, j, 2);
					} else if (map[i][j] == '>') {
						tank = new Tank(i, j, 3);
					} 
				}
			}
			
			int n = Integer.parseInt(br.readLine());
			String input = br.readLine();
			for (int i = 0; i < n; i++) {
				char cmd = input.charAt(i);
				switch (cmd) {
				case 'U':   // 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
					tank.dir = 0;
					if (tank.r - 1 >= 0) {
						if (map[tank.r-1][tank.c] == '.') {
							map[tank.r][tank.c] = '.';
							tank.r -= 1;
						}
					}
					map[tank.r][tank.c] = '^';
					break;
				case 'D':   // 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
					tank.dir = 1;
					if (tank.r + 1 < h) {
						if (map[tank.r+1][tank.c] == '.') {
							map[tank.r][tank.c] = '.';
							tank.r += 1;
						}
					}
					map[tank.r][tank.c] = 'v';
					break;
				case 'L':   // 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
					tank.dir = 2;
					if (tank.c - 1 >= 0) {
						if (map[tank.r][tank.c-1] == '.') {
							map[tank.r][tank.c] = '.';
							tank.c -= 1;
						}
					}
					map[tank.r][tank.c] = '<';
					break;
				case 'R':   // 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
					tank.dir = 3;
					if (tank.c + 1 < w) {
						if (map[tank.r][tank.c+1] == '.') {
							map[tank.r][tank.c] = '.';
							tank.c += 1;
						}
					}
					map[tank.r][tank.c] = '>';
					break;
				case 'S':   // 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
					int cr = tank.r, cc = tank.c;
					while (true) {
						int nr = cr + dxy[tank.dir][0], nc = cc + dxy[tank.dir][1];
						if (nr < 0 || nr >= h || nc < 0 || nc >= w) break;
						if (map[nr][nc] == '*') {	// 포탄이 벽돌과 충돌
							map[nr][nc] = '.';
							break;
						}
						if (map[nr][nc] == '#') break;	// 포탄이 강철과 충돌
						cr = nr;
						cc = nc;
					}
					break;
				default:
					break;
				}
			}
			
			StringBuilder sb = new StringBuilder();
			sb.append("#").append(test_case).append(" ");
			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					sb.append(map[i][j]);
				}
				sb.append("\n");
			}
			System.out.print(sb);
		}
	}
}
