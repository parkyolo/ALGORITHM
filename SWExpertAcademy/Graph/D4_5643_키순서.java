package SWExpertAcademy.Graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class D4_5643_키순서 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= t; test_case++) {
            int n = Integer.parseInt(br.readLine());
            int m = Integer.parseInt(br.readLine());

            // matrix[i][0] : i보다 작은 노드
            // matrix[i][1] : i보다 큰 노드
            ArrayList<Integer>[][] matrix = new ArrayList[n+1][2];
            for (int i = 1; i <= n; i++) {
                matrix[i][0] = new ArrayList<>();
                matrix[i][1] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                matrix[a][0].add(b);
                matrix[b][1].add(a);
            }

            int ans = 0;

            // i보다 작은 노드 + i보다 큰 노드의 수가 n-1이어야 순서를 정확히 알 수 있음
            for (int i = 1; i <= n; i++) {
                Queue<Integer> queue = new ArrayDeque<>();
                boolean[] visited = new boolean[n+1];
                visited[i] = true;
                int cnt = 0;

                // i보다 작은 노드 개수 세기
                queue.offer(i);
                while (!queue.isEmpty()) {
                    int cur = queue.poll();
                    for (int next : matrix[cur][0]) {
                        if (!visited[next]) {
                            visited[next] = true;
                            cnt++;
                            queue.offer(next);
                        }
                    }
                }

                // i보다 큰 노드 개수 세기
                queue.offer(i);
                while (!queue.isEmpty()) {
                    int cur = queue.poll();
                    for (int next : matrix[cur][1]) {
                        if (!visited[next]) {
                            visited[next] = true;
                            cnt++;
                            queue.offer(next);
                        }
                    }
                }

                if (cnt == n-1) ans++;
            }

            System.out.println("#" + test_case + " " + ans);
        }
    }
}
