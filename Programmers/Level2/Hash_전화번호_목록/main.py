def solution(phone_book):
    n = len(phone_book)
    phone_book.sort(key=lambda x:len(x))
    sub_str = [dict() for _ in range(len(phone_book[-1])+1)]
    
    for i in range(n):
        cur = phone_book[i]
        for j in range(len(phone_book[0]), len(cur)+1):
            if sub_str[j].get(cur[:j], False): return False
        sub_str[len(cur)][cur] = True
         
    return True

print(solution(["119", "97674223", "1195524421"]), False)
print(solution(["123", "456", "789"]), True)
print(solution(["12", "123", "1235", "567", "88"]), False)