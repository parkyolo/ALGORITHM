/*
 * 1. summary
 * 임의의 노드에 연산자가 있으면 자식 노드의 숫자를 이용해 연산한다.
 * 사칙연산 "+, -, *, /"와 양의 정수로만 구성된 이진 트리가 유효한지 검사한다.
 * 
 * 2. strategy
 * 리프 노드는 모두 숫자이고 그 외의 노드는 연산자여야 한다.
 * StringTokenizer로 input을 토큰화하여 리프 노드인지 아닌지 알아내고, 유효한지 체크한다.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D4_1233_Validation {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = 10;
		
		for (int test_case = 1; test_case <= t; test_case++) {
			int n = Integer.parseInt(br.readLine());
			StringTokenizer st;
			
			int answer = 1;
			
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				if (answer == 0) continue;
				st.nextToken();
				String token = st.nextToken();
				if (st.countTokens() == 0) {        // 리프 노드가 연산자이면 유효하지 않다.
					if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
						answer = 0;
					}
				} else if (st.countTokens() == 1) { // 자식 노드가 하나밖에 없으면 유효하지 않다.
					answer = 0;
				} else {                            // 중간 노드가 연산자가 아니면 유효하지 않다.
					if (!token.equals("+") && !token.equals("-") && !token.equals("*") && !token.equals("/")) {
						answer = 0;
					}
					
				}
			}
			System.out.println("#" + test_case + " " + answer);
		
		}
	}

}
