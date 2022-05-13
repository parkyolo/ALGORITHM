import java.util.Queue;
import java.util.LinkedList;
import java.awt.Point;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Queue<Point> queue = new LinkedList<Point>();
        queue.add(new Point(numbers[0], 0));
        queue.add(new Point(numbers[0]*(-1), 0));
        while (!queue.isEmpty()) {
            Point num = queue.poll();
            if (num.y == numbers.length-1) {
                if (num.x == target)
                    answer++;
                continue;
            }
            queue.add(new Point(num.x+numbers[num.y+1], num.y+1));
            queue.add(new Point(num.x-numbers[num.y+1], num.y+1));
        }
        
        return answer;
    }
}