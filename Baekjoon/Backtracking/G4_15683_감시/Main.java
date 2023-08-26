package Baekjoon.Backtracking.G4_15683_감시;

/*
 * 1. summary
 * n*m 공간에 5가지 종류의 cctv가 최대 8개 설치되어 있다.
 * cctv가 감시할 수 없는 사각지대의 최소 크기를 구한다.
 * 
 * 2. strategy
 * k개의 cctv의 가능한 방향 조합을 구한다.
 * 해당 방향으로 탐색하여 사각지대의 개수를 구한다.
 * 영역이 1~6이면 사각지대가 될 수 없으므로 처음부터 사각지대 수에서 뺀다.
 * 감시할 수 있는 위치를 방문하면서 visited 배열에 방문체크하고 사각지대 수에서 뺀다.
 * 모든 조합에 대해 탐색하며 최소 개수를 구한다.
 * 
 * */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.ArrayList;
 import java.util.StringTokenizer;
 
 class CCTV {
     int r, c, num;
 
     public CCTV(int r, int c, int num) {
         this.r = r;
         this.c = c;
         this.num = num;
     }
     
 }
 
 public class Main {
     
     private static int n, m, k;	// 세로, 가로 크기, cctv 수
     private static int minArea, notAreaCnt;	// 사각시대 최소 크기, cctv이거나 벽인 곳의 수
     private static int map[][];
     private static ArrayList<CCTV> cctv;	// cctv의 위치와 번호
     private static int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
     private static int[][][] dir = {// cctv가 감시할 수 있는 방향
         {},
         {{0}, {1}, {2}, {3}},
         {{0, 1}, {2, 3}},
         {{0, 3}, {3, 1}, {1, 2}, {2, 0}},
         {{2, 3, 0}, {3, 0, 1}, {1, 2, 3}, {0, 1, 2}},
         {{0, 1, 2, 3}}
     };
     private static int combi[];	// combi[i]: i번 cctv의 방향
 
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(br.readLine());
         n = Integer.parseInt(st.nextToken());
         m = Integer.parseInt(st.nextToken());
         
         map = new int[n][m];
         cctv = new ArrayList<CCTV>();
         
         notAreaCnt = 0;
         for (int i = 0; i < n; i++) {
             st = new StringTokenizer(br.readLine());
             for (int j = 0; j < m; j++) {
                 map[i][j] = Integer.parseInt(st.nextToken());
                 if (map[i][j] != 0) {
                     notAreaCnt++;
                     if (map[i][j] != 6) cctv.add(new CCTV(i, j, map[i][j]));
                 }
             }
         }
         
         k = cctv.size();
         minArea = Integer.MAX_VALUE;
         combi = new int[k];
         getOrder(0);
         System.out.println(minArea);
     }
 
     private static void getOrder(int cnt) {// cnt: 몇 번째 cctv인지
         if (cnt == k) {
             watch();
             return;
         }
         
         CCTV c = cctv.get(cnt);
         for (int i = 0; i < dir[c.num].length; i++) {
             combi[cnt] = i;	// cnt번째 cctv의 방향 i 설정
             getOrder(cnt+1);
         }
     }
 
     private static void watch() {	// 감시
         boolean[][] visited = new boolean[n][m];
         int area = n*m - notAreaCnt;
         
         for (int i = 0; i < k; i++) {
             CCTV c = cctv.get(i);
             for (int d : dir[c.num][combi[i]]) {	// d: 현재 cctv의 방향
                 int cr = c.r, cc = c.c;
                 while (true) {	// 감시할 수 있는 영역 체크
                     int nr = cr + dxy[d][0], nc = cc + dxy[d][1];
                     if (nr < 0 || nr >= n || nc < 0|| nc >= m) break;
                     if (map[nr][nc] == 6) break;
                     if (map[nr][nc] == 0 && !visited[nr][nc]) {
                         visited[nr][nc] = true;
                         area -= 1;
                     }
                     
                     cr = nr;
                     cc = nc;
                 }
             }
         }
         
         minArea = Math.min(minArea, area);
     }
 
 }
 