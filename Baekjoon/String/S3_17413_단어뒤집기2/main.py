def main():
    S = input()

    answer = ""
    sub_word = ""
    tag = False

    for s in S:
        if tag or s == "<" or s == ">": # 태그일 때
            if sub_word: # 이전 단어가 있다면
                answer += sub_word[::-1] # 단어 뒤집기
                sub_word = ""
            tag = True
            answer += s
            if s == ">": tag = False
        elif s == " ": # 공백일 때
            answer += sub_word[::-1] + s # 단어 뒤집기
            sub_word = ""
        else: # 단어일 때
            sub_word += s

    if sub_word:
        answer += sub_word[::-1]

    print(answer)

if __name__ == "__main__":
    main()