/*
 * 1. summary: 문제 해석
 * A, C, G, T로만 이루어진 문자열의 부분 문자열을 구한다.
 * 부분 문자열은 A, C, G, T가 입력으로 주어진 개수만큼 포함되어 있어야 한다.
 * 
 * 2. strategy: 풀이전략
 * key-value 쌍으로 A, C, G, T의 개수를 저장한다.
 * 부분문자열에 포함된 문자의 개수가 특정 개수 이상인지 검사하고 유효하면 카운트한다.
 * index를 증가시키면서 이전 문자열의 마지막 문자는 1 감소시키고 다음 문자의 개수를 1 증가시킨다.
 * 
 * 3. note: 주의할 사항(특이사항)
 * 부분 문자열은 연속된 문자열이다.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class S2_12891_DNAPassword {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int dnaStrLen = Integer.parseInt(input[0]);
        int pwLen = Integer.parseInt(input[1]);
        
        String dnaStr = br.readLine();
        
        Map<Character, Integer> selectedCnt = new HashMap<>();
        String[] minCntInput = br.readLine().split(" ");
        Map<Character, Integer> minCnt = new HashMap<>();
        
        char[] dna = {'A', 'C', 'G', 'T'};
        for (int i = 0; i < 4; i++) {
            minCnt.put(dna[i], Integer.parseInt(minCntInput[i]));
            selectedCnt.put(dna[i], 0);
        }
        
        int subStrCnt = 0;
        int i = 0;
        
        while (i < dnaStrLen) {
            if (i == 0) {
                for (int j = 0; j < pwLen; j++) {
                    char curChar = dnaStr.charAt(j);
                    selectedCnt.put(curChar, selectedCnt.get(curChar)+1);
                }
                i = pwLen;
            } else {
                char frontChar = dnaStr.charAt(i-pwLen);
                char rearChar = dnaStr.charAt(i);
                selectedCnt.put(frontChar, selectedCnt.get(frontChar)-1);
                selectedCnt.put(rearChar, selectedCnt.get(rearChar)+1);
                i++;
            }
            
            boolean isValidPW = true;
            for (int j = 0; j < 4; j++) {
                if (selectedCnt.get(dna[j]) < minCnt.get(dna[j])) {
                    isValidPW = false;
                    break;
                }
            }
            if (isValidPW) {
                subStrCnt++;
            }
        }
        
        System.out.println(subStrCnt);
        
    }

}
