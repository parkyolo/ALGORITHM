import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        HashMap<String, String> map = new HashMap<>();
        
        for (String re:record) {
            String[] re_list = re.split(" ");
            String cmd = re_list[0];
            String uid = re_list[1];
            if (cmd.equals("Enter") || cmd.equals("Change")) {
                String nickname = re_list[2];
                map.put(uid, nickname);
            }
        }
        
        for (String re:record) {
            String[] re_list = re.split(" ");
            String cmd = re_list[0];
            String uid = re_list[1];
            if (cmd.equals("Enter")) {
                answer.add(String.format("%s님이 들어왔습니다.", map.get(uid)));
            } else if (cmd.equals("Leave")) answer.add(String.format("%s님이 나갔습니다.", map.get(uid)));
        }
        
        String[] ans = answer.toArray(new String[answer.size()]);
        return ans;
    }
}