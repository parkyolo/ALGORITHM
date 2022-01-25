import math
def solution(fees, records):
    answer = []

    parking = {}
    parking_time = {} # 누적 주차 시간

    for record in records:
        time, number, inout = record.split(" ")
        time = int(time[:2])*60+int(time[3:])
        if inout == "IN": parking[number] = time
        else: 
            try:
                parking_time[number] += time - parking[number]
            except:
                parking_time[number] = time - parking[number]
            del parking[number]
    for number, time in parking.items():
        try:
            parking_time[number] += 1439 - time
        except:
            parking_time[number] = 1439 - time
    
    parking_fee = [] # [차량 번호, 주차 요금]
    for number, time in parking_time.items():
        if time < fees[0]: parking_fee.append([int(number), fees[1]])
        else: parking_fee.append([int(number), fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3]])
    
    parking_fee.sort(key=lambda x:x[0])
    for number, fee in parking_fee:
        answer.append(fee)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]), [14600, 34400, 5000])
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]), [0, 591])
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]), [14841])