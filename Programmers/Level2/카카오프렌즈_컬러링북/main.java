import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        boolean[][] v = new boolean[m][n];
        Queue<Integer> queuex = new LinkedList<>();
        Queue<Integer> queuey = new LinkedList<>();
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !v[i][j]){
                    queuex.offer(i);
                    queuey.offer(j);
                    v[i][j] = true;
                    int cur_id = picture[i][j];
                    int cnt = 1;
                    while (!queuex.isEmpty()) {
                        int x = queuex.poll();
                        int y = queuey.poll();
                        for (int d = 0; d < 4; d++) {
                            if (x+dx[d] >= 0 && x+dx[d] < m && y+dy[d] >= 0 && y+dy[d] <n) {
                                if (picture[x+dx[d]][y+dy[d]] == cur_id && !v[x+dx[d]][y+dy[d]]) {
                                    queuex.offer(x+dx[d]);
                                    queuey.offer(y+dy[d]);
                                    cnt ++;
                                    v[x+dx[d]][y+dy[d]] = true;
                                }
                            }

                        }
                    }
                    numberOfArea ++;
                    if (cnt > maxSizeOfOneArea) {
                        maxSizeOfOneArea = cnt;
                }
                
                }
                
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}