/*
 * 1. summary: 문제 해석
 * '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.
 * 이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별한다.
 * 
 * 2. strategy: 풀이전략
 * 여는 괄호는 stack에 넣는다.
 * 닫는 괄호가 나오면 stack을 pop하여 짝이 맞는지 확인한다.
 * 짝이 맞지 않거나 stack의 값이 남으면 0을 출력한다.
 * 
 * 3. note: 주의할 사항(특이사항)
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class D4_1218_ParenthesisMatching {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = 10;
        
        for (int test_case = 1; test_case < t+1; test_case++) {
            int n = Integer.parseInt(br.readLine());
            String input = br.readLine();
            Stack<Character> stack = new Stack<>();
            int valid = 1;
            
            checkValid:
            for (int i = 0; i < n; i++) {
                char token = input.charAt(i);
                switch(token) {
                case '(':
                case '[':
                case '{':
                case '<':
                    stack.push(token);
                    break;
                case ')':
                    if (stack.pop() != '(') {
                        valid = 0;
                        break checkValid;
                    }
                    break;
                case ']':
                    if (stack.pop() != '[') {
                        valid = 0;
                        break checkValid;
                    }
                    break;
                case '}':
                    if (stack.pop() != '{') {
                        valid = 0;
                        break checkValid;
                    }
                    break;
                case '>':
                    if (stack.pop() != '<') {
                        valid = 0;
                        break checkValid;
                    }
                    break;
                }
            }
            
            if (!stack.isEmpty()) {
                valid = 0;
            }
            
            System.out.println("#" + test_case + " " + valid);
        }
    }

}
