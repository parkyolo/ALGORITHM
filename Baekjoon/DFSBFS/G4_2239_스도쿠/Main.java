package Baekjoon.DFSBFS.G4_2239_스도쿠;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

    private static int[][] board;
    private static ArrayList<Point> zeros;  // 빈 칸의 위치
    private static boolean flag = false;    // 완성된 보드를 출력했는지 확인하기 위한 flag

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		board = new int[9][9];
		
		for (int i = 0; i < 9; i++) {
			String line = br.readLine();
			for (int j = 0; j < 9; j++) {
				board[i][j] = line.charAt(j) - '0';
			}
		}

        // 빈 칸 위치 저장
        zeros = new ArrayList<>();
		
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] == 0) {
					zeros.add(new Point(i, j));
				}
			}
		}

        // 0번째 빈 칸부터 dfs로 스도쿠 채우기
        dfs(0);
    }

    public static void dfs(int idx) {

        if (flag) return;   // 이미 사전순으로 앞서는 보드를 출력했다면 return

        if (idx == zeros.size()) {
            flag = true;
            // 정답 출력
            for (int x = 0; x < 9; x++) {
                for (int y = 0; y < 9; y++) {
                    System.out.print(board[x][y]);
                }
                System.out.println();
            }
            return;
        }

        // 행과 열이 작은 순으로 작은 숫자부터 채움 (사전순)
        int i = zeros.get(idx).x, j = zeros.get(idx).y;
        		
		for (int num = 1; num <= 9; num++) {
            // 가로, 세로, 3x3 보드에 숫자가 있나 확인
			if (checkRow(i, j, num) && checkCol(i, j, num) && checkSquare(i, j, num)) {
                // 숫자가 없으면 빈칸 채우기
                board[i][j] = num;
                dfs(idx+1);
                board[i][j] = 0;
            }
		}
	}

    private static boolean checkRow(int i, int j, int num) {
        boolean visited[] = new boolean[10];
        for (int k = 0; k < 9; k++) {
            visited[board[i][k]] = true;
        }

        if (visited[num]) return false;

        return true;
    }

    private static boolean checkCol(int i, int j, int num) {
        boolean visited[] = new boolean[10];
        for (int k = 0; k < 9; k++) {
            visited[board[k][j]] = true;
        }

        if (visited[num]) return false;

        return true;
    }

    private static boolean checkSquare(int i, int j, int num) {
        boolean visited[] = new boolean[10];
        i = Math.floorDiv(i,3) * 3;
        j = Math.floorDiv(j,3) * 3;

        for (int k = i; k < i+3; k++) {
            for (int l = j; l < j+3; l++) {
                visited[board[k][l]] = true;
            }
        }

        if (visited[num]) return false;

        return true;
    }
}
