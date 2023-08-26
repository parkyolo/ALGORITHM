package SWExpertAcademy.Graph;

/*
 * 1. summary
 * N개의 섬을 모두 연결한다.
 * 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 환경 부담금을 지불해야한다.
 * 최소 환경 부담금을 소수 첫째 자리에서 반올림하여 정수 형태로 출력한다.
 * 
 * 2. strategy
 * 각 정점 간의 거리를 adjMatrix에 저장한다.
 * Prim 알고리즘으로 최단 거리를 구한다.
 * 
 * 3. notice
 * 64비트 double로 처리할 것
 */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.Arrays;
 import java.util.PriorityQueue;
 import java.util.Queue;
 import java.util.StringTokenizer;
 
 public class D4_1251_하나로 {
     
     static class Vertex implements Comparable<Vertex>{
         int node;
         double weight;	// 정점 번호, 트리 정점과 연결했을 때의 간선 비용
 
         public Vertex(int node, double weight) {
             this.node = node;
             this.weight = weight;
         }
 
         @Override
         public int compareTo(Vertex o) {
             return Double.compare(this.weight, o.weight);
         }
         
     }
 
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
         int t = Integer.parseInt(br.readLine());
         for (int test_case = 1; test_case <= t; test_case++) {
             int n = Integer.parseInt(br.readLine());
             
             double[][] adjMatrix = new double[n][n];
             int[][] island = new int[n][2];
             
             StringTokenizer xs = new StringTokenizer(br.readLine());
             StringTokenizer ys = new StringTokenizer(br.readLine());
             for (int i = 0; i < n; i++) {
                 island[i][0] = Integer.parseInt(xs.nextToken());
                 island[i][1] = Integer.parseInt(ys.nextToken());
             }
             
             double e = Double.parseDouble(br.readLine());	// 환경부담세율
             
             // 1. 섬 간의 거리 구하기
             for (int i = 0; i < n-1; i++) {
                 int x1 = island[i][0], y1 = island[i][1];
                 for (int j = i+1; j < n; j++) {
                     int x2 = island[j][0], y2 = island[j][1];
                     
                     double dist = Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2);
                     
                     adjMatrix[i][j] = dist;
                     adjMatrix[j][i] = dist;
                 }
             }
             
             // 2. Prim 알고리즘으로 최단거리 구하기
             boolean[] visited = new boolean[n];
             double[] minDist = new double[n];
             Queue<Vertex> queue = new PriorityQueue<>();
             
             Arrays.fill(minDist, Double.MAX_VALUE);	// 최솟값 갱신을 위해 큰 값으로 세팅
             minDist[0] = 0;	// 임의의 정점 0을 트리 구성의 시작으로 세팅
             queue.offer(new Vertex(0, minDist[0]));
             
             double result = 0;
             int minVertex = 0, cnt = 0;
             double min;
             
             while (!queue.isEmpty()) {
                 // step1. 미방문(비트리) 정점 중 최소 간선 비용의 정점을 선택
                 Vertex cur = queue.poll();
                 
                 minVertex = cur.node;
                 min = cur.weight;
                 if (visited[minVertex]) continue;
                 
                 // step2. 방문(트리) 정점에 추가
                 visited[minVertex] = true;
                 result += min;	// 신장트리 비용 누적
                 if (++cnt == n) break;
                 
                 // step3. 트리에 추가된 새로운 정점 기준으로 비트리 정점과의 간선 비용 고려
                 for (int i = 0; i < n; i++) {
                     if (!visited[i] && adjMatrix[minVertex][i] != 0 && minDist[i] > adjMatrix[minVertex][i]) {
                         minDist[i] = adjMatrix[minVertex][i];
                         queue.offer(new Vertex(i, minDist[i]));
                         
                     }
                 }
             }
             
             result *= e;
             System.out.println("#" + test_case + " " + Math.round(result));
         }
     }
 
 }
 