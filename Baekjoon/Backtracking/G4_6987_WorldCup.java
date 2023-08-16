import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 1. summary
 * 6개 국가가 한 번씩 경기를 치른다.
 * 각 나라의 승, 무, 패 수가 가능한 결과인지 판별한다.
 * 가능하면 1, 불가능하면 0을 출력한다.
 * 
 * 2. strategy
 * 6개의 국가가 두 국가씩 모든 경기를 하면 6C2 = 15번의 경기를 하게 된다.
 * 경기가 끝나면 한 경기당 2점씩 점수가 기록되므로 승패 수의 총 합은 30점이다.
 * 
 * 6개 팀의 승, 무, 패의 합이 30점인지 검사한다.
 * 30점이 맞다면 모든 가능한 매치 조합에 대해 승, 무, 패를 했을 경우를 확인한다.
 * 승, 무, 패 수에 맞게 15번 경기할 수 있다면 가능한 결과이다.
 * 
 */

public class G4_6987_WorldCup {
	
	// 15개 경기에서 매치하는 팀 정보
	static int[] team1 = {0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4};
	static int[] team2 = {1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5};
	
	// 6개 팀의 결과 저장 배열
	static int[] win, draw, lose;
	static boolean flag;


	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < 4; i++) {	// 4줄
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			flag = false;	// flag 초기화
			
			// 6개 팀의 승, 무, 패
			win = new int[6];
			draw = new int[6];
			lose = new int[6];
			
			int w = 0, d = 0, l = 0;	// 15경기의 승패 수
			
			for (int team = 0; team < 6; team++) {
				w += win[team] = Integer.parseInt(st.nextToken());
				d += draw[team] = Integer.parseInt(st.nextToken());
				l += lose[team] = Integer.parseInt(st.nextToken());
			}

			if (w + d + l != 30) {	// 총 15 경기 후에 승패 수 합이 30이 아니면
				flag = false;
			} else {
				check(0);	// 경기 횟수
			}
			
			if (flag) System.out.print("1 ");
			else System.out.print("0 ");
		}
	}

	// 경기 횟수별로 경기할 두 팀을 배열에서 꺼내서 3가지 경우를 확인해 봄
	private static void check(int match) {
		// 종료 조건: 모든 경기를 다 한 경우
		if (match == 15) {
			flag = true;
			return;
		}
		
		// 반복 조건: 경기를 아직 다 안한 경우 - 3가지 경우 비교
		int a = team1[match];
		int b = team2[match];
		
		// 1. a > b
		if (win[a] > 0 && lose[b] > 0) {
			win[a]--;
			lose[b]--;
			check(match+1);
			win[a]++;
			lose[b]++;
		}
		
		// 2. a < b
		if (win[b] > 0 && lose[a] > 0) {
			win[b]--;
			lose[a]--;
			check(match+1);
			win[b]++;
			lose[a]++;
		}
		
		// 3. a == b
		if (draw[a] > 0 && draw[b] > 0) {
			draw[a]--;
			draw[b]--;
			check(match+1);
			draw[a]++;
			draw[b]++;
		}
	}
	
}
