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
        start_time, end_time, title, tune = info.split(',')
        s_f, s_b = map(int,start_time.split(":"))
        e_f, e_b = map(int,end_time.split(":"))

        time = 0
        if e_b > s_b: time = e_b-s_b + 60*(e_f-s_f)
        else: time = 60*(e_f-s_f)-s_b+e_b

        tune = change(tune)
        music_played = (tune*(time//len(tune)+1))[:time]

        if m in music_played:
            if answer[1] == '(None)' or time > answer[1]:
                answer = (title, time)
    return answer[0]

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"HELLO")
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),"FOO")
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"WORLD")