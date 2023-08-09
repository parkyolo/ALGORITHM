/*
 * 1. summary
 * n개의 정수 x가 주어진다.
 * x가 0이면 배열에서 절댓값이 가장 작은 값을 출력하고, 0이 아니면 배열에 값을 넣는다.
 * 절댓값이 가장 작은 값이 여러 개이면 가장 작은 수를 출력한다.
 * 출력한 수는 배열에서 제거한다.
 * 
 * 2. strategy
 * 문제의 조건대로 정렬되도록 comparator를 작성한다. 
 * 
 * */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class S1_11286_AbstractHeap {

public static void main(String[] args) throws Exception {
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  int n = Integer.parseInt(br.readLine());
  
  PriorityQueue<Integer> queue = new PriorityQueue<>((o1, o2) -> {

    int diff = Math.abs(o1) - Math.abs(o2);
    if (diff == 0) {
      return o1 - o2;
    }
    
    return diff;

  });
  
  StringBuilder sb = new StringBuilder();
  for (int i = 0; i < n; i++) {
    int x = Integer.parseInt(br.readLine());
    
    if (x == 0) {
      if (queue.isEmpty()) {
        sb.append(0).append("\n");
      } else {
        sb.append(queue.poll()).append("\n");
      }
    } else {
      queue.offer(x);
    }
  }
  
  System.out.println(sb);
}

}
