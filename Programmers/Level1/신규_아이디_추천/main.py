def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    n = ""
    for i in range(len(new_id)):
        a = ord(new_id[i])
        if a == 45 or a == 95 or a == 46 or 48 <= a <= 57 or 65 <= a <= 90 or 97 <= a <= 122:
            n += new_id[i]
    new_id = n
    n = new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i-1] == '.' and new_id[i] == '.':
            continue
        else:
            n += new_id[i]
    new_id = n
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]

    return new_id

solution("123_.def")