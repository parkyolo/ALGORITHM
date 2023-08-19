/*
* 1. summary
* r*c 크기의 보드에 알파벳이 적혀있다.
* 좌측 상단(0,0)에서 출발하여 상하좌우로 이동할 수 있을 때
* 알파벳이 중복되지 않도록 최대 몇 칸 이동할 수 있는지 출력한다.
*
* 2. strategy
* 알파벳이 등장했는지 확인하기 위한 방문 체크 배열 visit을 만든다.
* (nr, nc)를 방문하거나 방문하지 않으면서 백트래킹으로 탐색한다.
*
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int r, c, maxCnt;
    private static int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private static char[][] board;
    private static boolean[] visit;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new char[r][c];
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        visit = new boolean[26];
        maxCnt = 0;
        visit[board[0][0]-'A'] = true;  // 알파벳 방문 체크
        dfs(0, 0,1);

        System.out.println(maxCnt);
    }

    private static void dfs(int cr, int cc, int cnt) {
        maxCnt = Math.max(maxCnt, cnt);

        for (int d = 0; d < 4; d++) {
            int nr = cr + dxy[d][0];
            int nc = cc + dxy[d][1];

            if (nr < 0 || nr >= r || nc < 0 || nc >= c) continue;
            if (visit[board[nr][nc]-'A']) continue;

            visit[board[nr][nc]-'A'] = true;
            dfs(nr, nc, cnt+1);
            visit[board[nr][nc]-'A'] = false;
        }
    }
}
