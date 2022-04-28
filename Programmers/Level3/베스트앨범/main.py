def solution(genres, plays):
    answer = []
    genre_info = dict() # 장르 : [전체 재생 횟수,[[고유 번호,재생 횟수], ...]]
    for num, info in enumerate(zip(genres, plays)):
        genre, play = info
        if genre in genre_info.keys():
            genre_info[genre][0] += play
            genre_info[genre][1].append([num, play])
        else:
            genre_info[genre] = [play, [[num, play]]]
    
    play_info = []
    for genre, info in genre_info.items(): # genre_info의 key와 value를 합쳐줌
        play_info.append([genre]+info)
    
    play_info.sort(key=lambda x:-x[1]) # 전체 재생 횟수로 내림차순 정렬
    for genre, play_cnt, song_info in play_info:
        song_info.sort(key=lambda x:(-x[1], x[0]))
        
        for idx in range(min(len(song_info), 2)): # 장르에 속한 곡이 하나이면 하나의 곡만 선택
            answer.append(song_info[idx][0]) # 고유 번호 append
    return answer