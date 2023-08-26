/*
 * 1. summary
 * N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
 * 그리드는 같은 색으로 이루어진 몇 개의 구역이로 이루어져 있다. 
 * 적록색약인 경우 R과 G를 같은 구역이라고 한다.
 * 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 출력한다.
 * 
 * 2. strategy
 * BFS로 구역의 수를 탐색한다.
 * 적록색약인 경우 R과 G를 같은 색이라고 본다.
 * 구역의 수를 저장하는 변수와 방문 체크를 하는 배열을 따로 만들어 구역의 수를 따로 구한다.
 * 
 * */

 import java.awt.Point;
 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.ArrayDeque;
 import java.util.Queue;
 
 public class Main {
 
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         int n = Integer.parseInt(br.readLine());
         
         char[][] map = new char[n][n];
         for (int i = 0; i < n; i++) {
             String line = br.readLine();
             for (int j = 0; j < n; j++) {
                 map[i][j] = line.charAt(j);
             }
         }
         
         int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
         
         int cnt1 = 0;	// 적록색약이 아닌 사람이 봤을 때 구역의 수
         int cnt2 = 0;	// 적록색약인 사람이 봤을 때 구역의 수
         
         boolean[][] visit1 = new boolean[n][n];	// 적록색약이 아닌 사람이 봤을 때 방문 체크
         boolean[][] visit2 = new boolean[n][n];	// 적록색약인 사람이 봤을 때 방문 체크
         
         for (int i = 0; i < n; i++) {
             for (int j = 0; j < n; j++) {
                 
                 // 적록색약이 아닌 사람이 봤을 때 구역의 수 구하기
                 if (!visit1[i][j]) {
                     cnt1++;
                     
                     Queue<Point> queue = new ArrayDeque<>();
                     queue.offer(new Point(i, j));
                     visit1[i][j] = true;
                     
                     char color = map[i][j];	// 현재 구역의 색
                     
                     while (!queue.isEmpty()) {
                         Point p = queue.poll();
                         for (int d = 0; d < 4; d++) {
                             int nx = p.x + dxy[d][0], ny = p.y + dxy[d][1];
                             
                             if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;	// 범위를 벗어난 경우
                             if (visit1[nx][ny]) continue;							// 이미 방문한 위치인 경우
                             if (map[nx][ny] != color) continue;						// 다른 색의 구역인 경우
                             
                             visit1[nx][ny] = true;
                             queue.offer(new Point(nx, ny));
                         }
                         
                     }
                 }
                 
                 // 적록색약인 사람이 봤을 때 구역의 수 구하기
                 if (!visit2[i][j]) {
                     cnt2++;
                     
                     Queue<Point> queue = new ArrayDeque<>();
                     queue.offer(new Point(i, j));
                     visit2[i][j] = true;
                     
                     char color = map[i][j];	// 현재 구역의 색
                     
                     while (!queue.isEmpty()) {
                         Point p = queue.poll();
                         for (int d = 0; d < 4; d++) {
                             int nx = p.x + dxy[d][0], ny = p.y + dxy[d][1];
                             
                             if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;	// 범위를 벗어난 경우
                             if (visit2[nx][ny]) continue;							// 이미 방문한 위치인 경우
                             if ((color == 'R' || color == 'G') && map[nx][ny] == 'B') continue;	// 다른 색의 구역인 경우 (R과 G는 같은 구역)
                             if (color == 'B' && (map[nx][ny] == 'R' || map[nx][ny] == 'G')) continue;
                             
                             visit2[nx][ny] = true;
                             queue.offer(new Point(nx, ny));
                         }
                     }
                 }
             }
         }
         
         System.out.println(cnt1 + " " + cnt2);
 
     }
 
 }
  