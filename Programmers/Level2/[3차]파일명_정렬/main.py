def solution(files):
    answer = []

    file_split = []
    numbers = "0123456789"

    # 파일명을 head와 number로 분리
    for i, file in enumerate(files):
        now = "h"
        h = n = ""
        for f in file:
            if now == "h" and f not in numbers:
                h += f
            elif now == "h" and f in numbers:
                now = "n"
                n += f
            elif now == "n" and f in numbers and len(n) < 5:
                n += f
            elif now == "n" and (f not in numbers or len(n) >= 5):
                now = "t"
        # 파일명, head, number를 배열에 넣음
        file_split.append((file,h.lower(),int(n)))

    # 배열을 head와 number를 기준으로 정렬
    file_split.sort(key=lambda x:(x[1], x[2]))
    # 정렬된 배열의 파일명을 answer에 넣음
    answer = [file[0] for file in file_split]

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]),["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]),["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])
print(solution(["img000012345", "img1.png","img2","IMG02"]),["img000012345", "img1.png","img2","IMG02"])