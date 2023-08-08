/*
 * 1. summary
 * n은 과자의 개수, m은 무게 합 제한을 나타낸다.
 * n개의 과자 중 두 봉지를 선택했을 때 무게 합이 m 이하이면서 최대일 때의 무게 합을 구한다.
 * 
 * 2. strategy
 * 2개씩 조합을 구해서 m 이하이면서 최대인 값을 구한다.
 * 
 * */

 import java.io.BufferedReader;
 import java.io.InputStreamReader;
 import java.util.StringTokenizer;
 
 public class D3_9229_SpotMart {
     private static int n, m, maxWeight;
     private static int[] weights;
 
     public static void main(String[] args) throws Exception{
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
         int t = Integer.parseInt(br.readLine());
         for (int test_case = 1; test_case <= t; test_case++) {
             StringTokenizer st = new StringTokenizer(br.readLine());
             n = Integer.parseInt(st.nextToken());
             m = Integer.parseInt(st.nextToken());
             
             st = new StringTokenizer(br.readLine());
             weights = new int[n];
             for (int i = 0; i < n; i++) {
                 weights[i] = Integer.parseInt(st.nextToken());
             }
             
             maxWeight = -1;
             getCombi(0, 0, 0);
             System.out.println("#" + test_case + " " + maxWeight);
         }
     }
     
     public static void getCombi(int cnt, int start, int weight) {
         if (cnt == 2) {
             if (weight <= m) {
                 maxWeight = Math.max(maxWeight, weight);
             }
             return;
         }
         
         for (int i = start; i < n; i++) {
             getCombi(cnt+1, i+1, weight+weights[i]);
         }
     }
 
 }
 
 