import sys
sys.setrecursionlimit(100000)

student_cnt, selected_student = 0, []
visited, vset = [], set()
cnt, flag = 0, False
target_num = 0

def dfs(cur_student):
    global cnt, flag, target_num

    if cur_student in vset:         # cycle을 이룰 경우
        flag = True
        target_num = cur_student    # cycle의 끝 점을 저장
        return
    elif visited[cur_student]:      # 이전에 확인한 번호일 경우
        return                      # 넘어감
    else:
        visited[cur_student] = True
        vset.add(cur_student)
        dfs(selected_student[cur_student])
        if flag:                            # cycle이 형성된 경우
            cnt += 1
            if cur_student == target_num:   # 현재 번호가 시작점일 경우
                flag = False                # cycle을 끝냄


def make_team():
    global visited, vset, cnt, flag
    visited = [False for _ in range(student_cnt+1)] # 방문 체크
    cnt = 0 # 팀을 이룬 학생 수
    for i in range(1, student_cnt+1):
        if visited[i]: continue
        vset = set() # i번부터 팀을 선택할 때 방문한 번호
        vset.add(i)

        flag = False # cycle을 이뤘는지 체크
        visited[i] = True

        dfs(selected_student[i]) # cycle 찾기

        if flag: # i번이 cycle의 시작일 경우
            cnt += 1

    print(student_cnt - cnt)


def main():
    global student_cnt, selected_student
    T = int(input())
    for _ in range(T):
        student_cnt = int(input()) # 학생의 수
        selected_student = [0] + list(map(int, input().split())) # 선택된 학생들의 번호
        make_team() # 팀 구성하기


if __name__ == "__main__":
    main()