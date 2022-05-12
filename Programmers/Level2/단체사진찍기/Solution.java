import java.util.Stack;
import java.lang.Math;

public class Solution {
    static int answer;
    static boolean[] v;
    static String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};
    
    public boolean check(Stack<String> permu, String[] data) {
        for (String d:data) {
            String from = d.substring(0,1);
            String to = d.substring(2,3);
            String oper = d.substring(3,4);
            int dist = Integer.parseInt(d.substring(4))+1;
            int dist1 = permu.indexOf(from);
            int dist2 = permu.indexOf(to);
            if (oper.equals("=")) {
                if (Math.abs(dist1 - dist2) != dist) return false;
            } else if (oper.equals(">")) {
                if (Math.abs(dist1 - dist2) <= dist) return false;
            } else {
                if (Math.abs(dist1 - dist2) >= dist) return false;
            }
        }
        return true;
    }
    
    public void dfs(int n, Stack<String> permu, String[] data) { // 순열 생성
        if (n == 8) {
            if (check(permu, data)) {
                answer ++;
                return;
            };
        }
        
        for (int i=0; i<8; i++) {
            if (!v[i]) {
                v[i] = true;
                permu.push(friends[i]);
                dfs(n+1, permu, data);
                v[i] = false;
                permu.pop();
            }
        }
    }
    
    public int solution(int n, String[] data) {
        answer = 0;
        v = new boolean[8];
        Stack<String> permu = new Stack<>();
        dfs(0, permu, data);
        
        return answer;
    }

    public static void main(String[] args) {
        int n = 2;
        String[] data = {"N~F=0", "R~T>2"};
        Solution sol = new Solution();
        int dab = sol.solution(n, data);
        System.out.println(String.format("%d 3648", dab));
    }
}


