package Baekjoon.TopologySort.G3_2252_줄세우기;
/*
 * 1. summary
 * 일부 학생의 키를 비교한 결과가 주어졌을 때, 학생들을 키 순서대로 출력한다.
 * 
 * 2. strategy
 * list[i]에 i번 학생 다음에 오는 학생 번호를 저장한다.
 * indegree[i]에 i번 학생 앞에 오는 학생 수(진입 차수)를 저장한다.
 * 앞에 다른 학생이 안오는 학생(진입 차수가 0인 노드)부터 queue에 넣고 순서대로 출력한다.
 * 출력된 학생의 다음으로 오는 학생(인접 노드)의 진입 차수를 감소시키고 0이 되면 다시 queue에 넣는다.
 * 
 */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.ArrayList;
 import java.util.LinkedList;
 import java.util.Queue;
 import java.util.StringTokenizer;
 
 public class Main {
 
     public static void main(String[] args) throws Exception {
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(br.readLine());
         int n = Integer.parseInt(st.nextToken());
         int m = Integer.parseInt(st.nextToken());
 
         int[] indegree = new int[n+1];
         ArrayList<Integer> graph[] = new ArrayList[n+1];
         for (int i = 1; i <= n; i++) {
             graph[i] = new ArrayList<Integer>();
         }
         
         for (int i = 0; i < m; i++) {
             st = new StringTokenizer(br.readLine());
             int a = Integer.parseInt(st.nextToken());
             int b = Integer.parseInt(st.nextToken());
             
             graph[a].add(b);
             indegree[b]++;
         }
         
         Queue<Integer> queue = new LinkedList<>();
         for (int i = 1; i <= n; i++) {
             if (indegree[i] == 0) {
                 queue.offer(i);
             }
         }
         
         StringBuilder sb = new StringBuilder();
         while (!queue.isEmpty()) {
             int curNode = queue.poll();
             sb.append(curNode + " ");
             for (int nextNode : graph[curNode]) {
                 indegree[nextNode]--;
                 if (indegree[nextNode] == 0) {
                     queue.offer(nextNode);
                 }
             }
         }
         
         System.out.println(sb);
     }
 
 }
  