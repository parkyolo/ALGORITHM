import sys
INF = sys.maxsize

def run():
    sm, sc, si = map(int, input().split()) # 메모리 크기, 프로그램 코드 크기, 입력의 크기
    programCode = list(input())
    input_ = input()

    bracket = {} # 괄호의 짝의 위치를 저장
    stack = []
    for i in range(sc):
        if programCode[i] == "[":
            stack.append(i)
        elif programCode[i] == "]":
            open, close = stack.pop(), i
            bracket[open] = close
            bracket[close] = open
    
    memory = [0 for _ in range(sm)]
    pointer = 0  # 포인터
    cmd = 0      # 명령어 인덱스
    inputIdx = 0 # 입력 인덱스

    cnt = 0     # 명령어 실행 횟수
    loop = INF  # 루프의 시작 위치
    
    while cmd < sc:
        cnt += 1
        if programCode[cmd] == "+":
            memory[pointer] = (memory[pointer] + 1) % 2**8
        elif programCode[cmd] == "-":
            memory[pointer] = (memory[pointer] - 1) % 2**8
        elif programCode[cmd] == "<":
            pointer = (pointer - 1) % sm
        elif programCode[cmd] == ">":
            pointer = (pointer + 1) % sm
        elif programCode[cmd] == "[":
            if memory[pointer] == 0:
                cmd = bracket[cmd]
        elif programCode[cmd] == "]":
            if memory[pointer] != 0:
                cmd = bracket[cmd]
        elif programCode[cmd] == ",":
            if inputIdx >= si:
                memory[pointer] = 255
            else:
                memory[pointer] = ord(input_[inputIdx])
                inputIdx += 1

        if cnt > 50000000: # 무한 루프가 생성될 때, 무한 루프의 시작점을 찾음
            loop = min(loop, cmd)
        if cnt > 50000000*2: # 최소 한 번의 무한 루프를 실행한 후 위치 출력
            return "Loops %d %d"%(loop, bracket[loop])

        cmd += 1

    return "Terminates" # 프로그램이 종료되는 경우

def main():
    t = int(input())

    for _ in range(t):
        print(run())

if __name__ == "__main__":
    main()