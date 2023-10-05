package SWExpertAcademy.DataStructures;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class 5658_TreasureChestPassword {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for (int test_case = 1; test_case <= t; test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			String nums = br.readLine();
			
			Queue<Integer> pq = new PriorityQueue<>();	// 수를 정렬할 큐
			Set<Integer> set = new HashSet<Integer>();	// 중복체크를 위한 셋
			
			int sidx = 0, eidx = n/4;	// 시작, 끝 인덱스
			int num = 0;				// 현재 숫자
			
			// 0~9는 숫자 그대로 더해주기 위해 char '0'을 빼주고
			// A~E는 10~15의 숫자를 더해주기 위해 char '7'을 빼줌
			for (int i = sidx; i < eidx; i++) {
				char tmp = '7';
				if (nums.charAt(i) - '7' < 10) tmp = '0';
				// 자릿수만큼 16진수로 환산해서 더한다.
				num += (nums.charAt(i) - tmp) * Math.pow(16, n/4-i-1);
			}

			pq.offer(-num);
			set.add(-num);
			
			// 다음 인덱스로 넘어감
			sidx = (sidx + 1) % n;	
			eidx = (eidx + 1) % n;
			
			// 시작인덱스가 0으로 돌아올 때까지 반복
			while (sidx != 0) {
				// 첫 번째 자리 숫자를 뺌
				char tmp = '7';
				if (nums.charAt(sidx-1) - '7' < 10) tmp = '0';
				num -= (nums.charAt(sidx-1) - tmp) * Math.pow(16, n/4-1);
				
				// 나머지 숫자를 왼쪽으로 쉬프트
				num *= 16;
				
				// 다음 자리 숫자를 더함
				tmp = '7';
				if (nums.charAt(eidx-1 < 0? eidx-1+n:eidx-1) - '7' < 10) tmp = '0';
				num += nums.charAt(eidx-1 < 0? eidx-1+n:eidx-1) - tmp;
				
				// 새로운 숫자가 set에 없으면 pq에 추가
				if (!set.contains(-num)) {
					pq.offer(-num);
					set.add(-num);
				}
				
				// 다음 인덱스로 넘어감
				sidx = (sidx + 1) % n;
				eidx = (eidx + 1) % n;
			}
			
			// k-1번째로 큰 숫자까지 pq에서 제거
			for (int i = 0; i < k-1; i++) {
				pq.poll();
			}

			// 정답 출력
			// 내림차순으로 정렬하기 위해 -1을 곱해줬으므로 -1을 곱한 숫자를 출력
			System.out.println("#" + test_case + " " + -pq.poll());
			
		}
	}

}
