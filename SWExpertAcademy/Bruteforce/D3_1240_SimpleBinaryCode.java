/*
 * [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
 * https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=JAVA&select-1=3&pageSize=10&pageIndex=1
 * 
 * 1. 암호코드가 포함된 행을 찾는다. ("1"이 포함된 행)
 * 2. 해석할 수 있는(codes에 key가 있는) 7개의 bit(암호 숫자)를 찾는다.
 * 3. 7 bits를 해석한 수를 sum과 number에 더한다.(홀수 자리인 경우 number에는 3을 곱해서 더한다.)
 * 4. 암호 숫자가 8번 연속되면 탐색을 종료한다.
 * 5. number가 10의 배수이면 올바른 암호코드이므로 10을 출력하고, 아니면 잘못된 암호코드이므로 0을 출력한다.
 */

import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Solution
{
    static Map<String, Integer> codes = new HashMap<String, Integer>() {{
        put("0001101", 0);
        put("0011001", 1);
        put("0010011", 2);
        put("0111101", 3);
        put("0100011", 4);
        put("0110001", 5);
        put("0101111", 6);
        put("0111011", 7);
        put("0110111", 8);
        put("0001011", 9);
    }};

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int n = sc.nextInt(), m = sc.nextInt();

            
            int sum = 0;    // sum of codes
            int number = 0; // sum of odd * 3 and even

            for (int j = 0; j < n; j++) { // row index
                String line = sc.next();
                if (sum > 0) continue;  // if already found the code, continue
                if (!line.contains("1")) continue;                               // 1. find the row that contains the codes (if the line doesn't contain a code, continue)
                
                String code;
                int start = 0;  // start index
                int i = 0;      // col index
                int cnt = 0;    // count of code(to determine if it's an odd or even number)
            
                while (i < m-7) {
                    if (cnt >= 8) break;                                            // 4. if already found 8 numbers, break
                    code = line.substring(i, i+7);  // the code consists of 7 bits
                    if (codes.containsKey(code)) {                                  // 2. if 7 bits are the code,
                        i += 7;
                        cnt += 1;

                        sum += codes.get(code);                                     // 3. add to sum and number
                        if (cnt % 2 == 1) number += codes.get(code) * 3;
                        else number += codes.get(code);

                    } else {    // if it's not a code number, return to start
                        i = ++start;
                        cnt = 0;
                        sum = 0;
                        number = 0;
                    }
                }
            }

            if (number % 10 == 0) System.out.println("#" + test_case + " " + sum);  // 5. if the password is correct, print the sum
            else System.out.println("#" + test_case + " 0");                        //    if not, print 0
		}

        sc.close();
	}
}