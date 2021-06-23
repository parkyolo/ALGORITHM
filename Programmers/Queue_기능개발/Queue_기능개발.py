import math

def solution(progresses, speeds):
    answer = []
    while progresses:
        released = 0
        days = math.ceil((100-progresses[0])/speeds[0])
        progresses.pop(0)
        speeds.pop(0)
        released += 1
        while progresses:
            if progresses[0] + speeds[0] * days >= 100:
                released += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                for i in range(len(progresses)):
                    progresses[i] += speeds[i] * days
                break
        answer.append(released)
    return answer

answer = solution([93, 30, 55], [1, 30, 5])
print(answer) #[2, 1]