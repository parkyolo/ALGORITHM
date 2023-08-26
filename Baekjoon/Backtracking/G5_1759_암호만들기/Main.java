package Baekjoon.Backtracking.G5_1759_암호만들기;

/*
 * 1. summary
 * 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다.
 * 암호를 이루는 알파벳은 암호에서 증가하는 순서로 배열된다.
 * C개의 문자가 주어졌을 때, 가능성 있는 암호들을 모두 출력한다.
 * 
 * 2. strategy
 * 알파벳을 정렬한다.
 * 가능한 암호 조합을 만든다.
 * 조건에 부합하면 출력한다.
 * 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int l, c;
    private static char alpha[], combi[];
    private static StringBuilder answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        alpha = new char[c];
        for (int i = 0; i < c; i++) {
            alpha[i] = st.nextToken().charAt(0);
        }

        Arrays.sort(alpha);

        answer = new StringBuilder();
        combi = new char[l];
        getCombi(0, 0);
        System.out.println(answer);
    }

    private static void getCombi(int cnt, int start) {
        if (cnt == l) {
            check();
            return;
        }

        for (int i = start; i < c; i++) {
            combi[cnt] = alpha[i];
            getCombi(cnt+1, i+1);
        }
    }

    private static void check() {
        int vowel = 0;	// 자음
        int conso = 0;	// 모음

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < l; i++) {
            if (combi[i] == 'a' || combi[i] == 'e' || combi[i] == 'i' || combi[i] == 'o' || combi[i] == 'u') {
                conso++;
            } else {
                vowel++;
            }
            sb.append(combi[i]);
        }

        if (vowel < 2 || conso < 1) return;
        answer.append(String.valueOf(sb)).append("\n");
    }

}
