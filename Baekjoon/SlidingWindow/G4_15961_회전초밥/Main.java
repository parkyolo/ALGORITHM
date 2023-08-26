package Baekjoon.SlidingWindow.G4_15961_회전초밥;

/*
 * 1. summary
 * 손님은 연속된 k개의 초밥을 먹는다.
 * k개 안에 c번 초밥이 없다면 c번 초밥을 추가로 먹는다.
 * 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구한다.
 * 
 * 2. strategy
 * k개의 연속된 초밥의 첫 번째를 가리키는 index인 s와 마지막을 가리키는 index인 e를 이동하면서 초밥의 개수를 센다.
 * s번째 초밥이 1개 남았다면 가짓수를 감소하고 e번째 초밥이 1개 생기면 가짓수를 증가한다.
 * k개 안에 c번 초밥이 없으면 가짓수에 1을 더한다.
 * 가짓수의 최댓값으로 답을 갱신한다.
 * 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());	// 벨트에 놓인 접시 수 (간선 수)
        int d = Integer.parseInt(st.nextToken());	// 초밥의 가짓 수 (정점 수)
        int k = Integer.parseInt(st.nextToken());	// 연속해서 먹는 접시 수
        int c = Integer.parseInt(st.nextToken());	// 쿠폰 번호

        int[] belt = new int[n];
        for (int i = 0; i < n; i++) {
            belt[i] = Integer.parseInt(br.readLine());
        }

        int[] visited = new int[d+1];   // 방문 횟수
        int cnt = 0;    // 초밥 가짓수

        for (int i = 0; i < k; i++) {
            if (visited[belt[i]] == 0) cnt++;
            visited[belt[i]]++;
        }

        int s = 0, e = k;
        int answer = visited[c] == 0 ? cnt+1 : cnt;

        for (int i = 0; i < n; i++) {
            if (visited[belt[s]] == 1) cnt--;
            visited[belt[s]]--;

            if (visited[belt[e]] == 0) cnt++;
            visited[belt[e]]++;

            s = (s+1) % n;
            e = (e+1) % n;

            if (visited[c] == 0) answer = Math.max(answer, cnt+1);
            if (visited[c] != 0) answer = Math.max(answer, cnt);
        }

        System.out.println(answer);
    }

}
