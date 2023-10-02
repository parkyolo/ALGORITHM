package Baekjoon.DFSBFS.G4_3055_탈출;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Hedgehog {
    int x, y, cnt;

    public Hedgehog(int x, int y, int cnt) {
        this.x = x;
        this.y = y;
        this.cnt = cnt;
    }
}

public class Main {

    private static int r, c;
    private static int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private static char[][] map;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        map = new char[r][c];
        int sx = 0, sy = 0; // 고슴도치의 시작 위치
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                map[i][j] = line.charAt(j);
                if (map[i][j] == 'S') {
                    sx = i;
                    sy = j;
                }
            }
        }

        // 비버의 굴에 도착할 수 없는 경우
        if (!bfs(sx, sy)) System.out.println("KAKTUS");
    }

    private static boolean bfs(int sx, int sy) {
        Queue<Hedgehog> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[r][c];
        queue.offer(new Hedgehog(sx, sy, 0));
        visited[sx][sy] = true;

        int time = 0;   // 경과 시간

        while (!queue.isEmpty()) {
            Hedgehog h = queue.poll();
            int cx = h.x, cy = h.y;

            if (map[cx][cy] == 'D') {   // 비버 굴 도착
                System.out.println(h.cnt);
                return true;
            }

            if (h.cnt > time) { // time분에 이동할 수 있는 위치를 모두 지났으면 시간이 경과되고 물이 흐른다.
                time++;
                flow();
            }

            for (int d = 0; d < 4; d++) {
                int nx = cx + dxy[d][0], ny = cy + dxy[d][1];

                if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;   // 범위 체크
                if (map[nx][ny] == 'X' || map[nx][ny] == '*') continue; // 돌이나 물로는 이동할 수 없음
                if (visited[nx][ny]) continue;  // 방문 체크
                if (map[nx][ny] != 'D' && !check(nx, ny)) continue; // 도착 지점이 아닌 경우, 물이 찰 예정인 칸인지 검사

                visited[nx][ny] = true;
                queue.offer(new Hedgehog(nx, ny, h.cnt+1));
            }
        }
        return false;
    }

    private static boolean check(int x, int y) {    // (x, y)가 물이 찰 예정인 칸이면 false 반환
        for (int d = 0; d < 4; d++) {
            int nx = x + dxy[d][0], ny = y + dxy[d][1];
            if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
            if (map[nx][ny] == '*') return false;
        }
        return true;
    }

    private static void flow() {    // 물과 인접한 칸에 물을 채운다.
        Queue<Point> flowarea = new ArrayDeque<>();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (map[i][j] == '*') {
                    for (int d = 0; d < 4; d++) {
                        int nx = i + dxy[d][0], ny = j + dxy[d][1];
                        if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
                        if (map[nx][ny] == '.') flowarea.offer(new Point(nx, ny));
                    }
                }
            }
        }

        while (!flowarea.isEmpty()) {
            Point p = flowarea.poll();
            map[p.x][p.y] = '*';
        }
    }
}
