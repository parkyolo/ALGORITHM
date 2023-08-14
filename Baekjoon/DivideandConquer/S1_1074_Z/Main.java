/*
 * 1. summary
 * 크기가 2^N * 2^N인 2차원 배열을 Z모양(왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문)으로 탐색하려고 한다.
 * N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력한다.
 * 
 * 2. strategy
 * (sr, sc)에서 시작해서 한 변이 size인 배열 안에 (r, c)가 존재하는지 확인한다.
 * 배열 안에 (r, c)가 존재하지 않으면 바로 return한다.
 * 배열 안에 (r, c)가 존재하면 배열을 4등분하여 탐색한다.
 * 이 때, num은 기존의 num에 나눠진 배열의 원소 수 만큼 더해진다.
 * sr == r, sc == r이 되면 num이 답이 된다.
 * 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	private static int r, c;
	private static int answer;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		getOrder(0, 0, (int) Math.pow(2, n), 0);
		System.out.println(answer);
	}

	private static void getOrder(int sr, int sc, int size, int num) {
		if (r == sr && c == sc) {
			answer = num;
			return;
		} else if (r < sr || r >= sr+size || c < sc || c >= sc+size) return;
		
		int half = size/2;
		getOrder(sr, sc, half, num);
		getOrder(sr, sc+half, half, num + half*half);
		getOrder(sr+half, sc, half, num + 2*half*half);
		getOrder(sr+half, sc+half, half, num + 3*half*half);
		
	}
}
