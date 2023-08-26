package Baekjoon.Implementation.G1_17143_낚시왕;

/*
 * 1. summary
 * - 낚시왕이 오른쪽으로 한 칸 이동한다.
 * - 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
 * - 상어가 이동한다.
 * 낚시왕이 오른쪽 끝 칸으로 이동을 마쳤을 때 낚시왕이 잡은 상어 크기의 합을 구한다.
 * 
 * 2. strategy
 * - 사람의 열 위치(pc)를 오른쪽으로 한 칸 이동한다.
 * - 상어 중 pc열에 있으면서 r이 가장 작은 상어의 크기를 더하고 삭제한다.
 * - 상어를 이동한다.
 * 	- 상어가 이동을 시작하는 위치와 방향을 고정한다.
 * 	- 한 번 왕복하는 범위로 이동 횟수를 줄인다.
 * 	- 이동 횟수가 격자의 길이를 넘어가면 방향을 바꾼다.
 * 
 * */

 import java.awt.Point;
 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.ArrayList;
 import java.util.List;
 import java.util.StringTokenizer;
 
 public class Main {
 
     static class Shark {
         int r, c, s, d, z;	// 위치, 속력, 이동방향, 크기
 
         public Shark(int r, int c, int s, int d, int z) {
             this.r = r;
             this.c = c;
             this.s = s;
             this.d = d;
             this.z = z;
         }
     }
     
     static int[][] dxy = {{}, {-1, 0}, {1, 0}, {0, 1}, {0, -1}};	// 위, 아래, 오른쪽, 왼쪽
     static int R, C, M;
     static Shark map[][];
     
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(br.readLine());
         R = Integer.parseInt(st.nextToken());
         C = Integer.parseInt(st.nextToken());
         M = Integer.parseInt(st.nextToken());	// 상어의 수
         
         map = new Shark[R+1][C+1];
         for (int i = 0; i < M; i++) {
             st = new StringTokenizer(br.readLine());
             int r = Integer.parseInt(st.nextToken());
             int c = Integer.parseInt(st.nextToken());
             int s = Integer.parseInt(st.nextToken());
             int d = Integer.parseInt(st.nextToken());
             int z = Integer.parseInt(st.nextToken());
             map[r][c] = new Shark(r, c, s, d, z);
         }
         
         int pc = 0;	// 낚시왕의 시작 위치
         int sum = 0;
         
         while (pc < C) {
             // 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
             pc++;	
             
             // 2. 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
             for (int i = 1; i <= R; i++) {
                 if (map[i][pc] != null) {
                     sum += map[i][pc].z;
                     map[i][pc] = null;
                     break;
                 }
             }
             
             // 3. 상어가 이동한다.
             moveShark();
         }
         
         System.out.println(sum);
     } 
 
     private static void moveShark() {
         List<Shark> nextPosition = new ArrayList<>();
         
         for (int i = 1; i <= R; i++) {
             for (int j = 1; j <= C; j++) {
                 if (map[i][j] != null) {
                     Shark cur = map[i][j];
                     // 상하로 움직이기
                     if (cur.d == 1 || cur.d == 2) {
                         Point next = getPosition(R, cur.r, cur.s, cur.d);
                         cur.r = next.x;
                         cur.d = next.y;
                     }
                     // 좌우로 움직이기
                     else {
                         Point next = getPosition(C, cur.c, cur.s, cur.d);
                         cur.c = next.x;
                         cur.d = next.y;
                     }
                     // 다음 위치로 이동하기 위해 현재 위치에서 삭제
                     map[i][j] = null;
                     nextPosition.add(cur);
                 }
             }
         }
         
         // 다음 위치로 이동
         for (Shark shark : nextPosition) {
             if (map[shark.r][shark.c] != null) {
                 // 한 칸에 상어가 두 마리 이상 있을 때 크기가 가장 큰 상어만 남음
                 if (map[shark.r][shark.c].z < shark.z) {
                     map[shark.r][shark.c] = shark;
                 }
             } else {
                 map[shark.r][shark.c] = shark;
             }
             
         }
     }
 
     // rc: 방향이 위나 아래면 행의 길이, 오른쪽이나 왼쪽이면 열의 길이
     // x: 방향이 위나 아래면 상어의 행 위치, 오른쪽이나 왼쪽이면 상어의 열 위치
     // s: 상어의 속력
     // dir: 상어의 방향
     static Point getPosition(int rc, int x, int s, int dir) {
         
         // 상어를 0번 행이나 0번 열에 고정한다.
         // 원래 있던 위치만큼 뒤로 이동한 것처럼 앞으로 이동해야 할 칸 수(속력)에 더해준다.
         if (dir == 2 || dir == 3) s += x;
         if (dir == 1 || dir == 4) s += rc - x + rc;
         
         // 방향은 아래나 오른쪽으로 고정한다.
         dir = (dir == 1 || dir == 2) ? 2 : 3;
         
         // 0부터 격자 길이의 2배까지 움직이는 횟수를 고정한다.
         if (s > rc+(rc-1)) {
             s %= rc+rc-2 ;
             if (s == 0 || s == 1) s += rc+rc-2;
         }
         
         // s가 격자의 길이를 넘어가면 방향을 변경한다.
         if (s > rc) {
             dir = (dir == 2) ? 1 : 4;
             s = rc-s+rc;
         }
         
         // 이동할 위치와 방향 반환
         return new Point(s, dir);	
     }
 }
 