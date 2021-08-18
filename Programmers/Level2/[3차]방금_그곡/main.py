def change(music):
    if 'A#' in music: music = music.replace('A#', 'a')
    if 'C#' in music: music = music.replace('C#', 'c')
    if 'D#' in music: music = music.replace('D#', 'd')
    if 'F#' in music: music = music.replace('F#', 'f')
    if 'G#' in music: music = music.replace('G#', 'g')
    return music

def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)',0)

    for info in musicinfos:
        start_time, end_time, title, music = info.split(',')
        s_f, s_b = map(int,start_time.split(":"))
        e_f, e_b = map(int,end_time.split(":"))

        time = 0 # 재생 시간
        if e_b > s_b: time = e_b-s_b + 60*(e_f-s_f)
        else: time = 60*(e_f-s_f)-s_b+e_b

        music = change(music)
        # 재싱된 곡
        music_played = (music*(time//len(music)+1))[:time]

        # 네오가 기억한 멜로디와 일치하는 곡일 경우
        if m in music_played:
            if answer[1] == '(None)' or time > answer[1]:
                answer = (title, time)
    return answer[0]

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"HELLO")
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),"FOO")
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"WORLD")