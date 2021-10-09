def solution(progresses,speeds):
    stack = list()
    answer = list()
    left_progresses = list()
    for i in progresses:
        left_progresses.append(100-i)
    while left_progresses:
        for i in range(len(left_progresses)):
            left_progresses[i]-=speeds[i]
        while left_progresses[0]<=0:
            stack.append(left_progresses.pop(0))
            speeds.pop(0)
            if len(left_progresses)==0:
                break
        if stack:
            answer.append(len(stack))
            stack=list()
    return answer

solution([93, 30, 55],[1, 30, 5])