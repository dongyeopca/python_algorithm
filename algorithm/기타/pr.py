def solution(dartResult):
    answer = 0
    stack = list()
    check_int = ""
    for i in dartResult:
        if i == "S":
            stack.append(int(check_int))
            check_int = ""
            continue
        elif i == "D":
            stack.append(int(check_int))
            check_int = ""
            stack[-1]=stack[-1]**2
        elif i == "T":
            stack.append(int(check_int))
            check_int = ""
            stack[-1]=stack[-1]**3
        elif i =="*":
            if len(stack) == 1:
                stack[-1] = stack[-1]*2
            elif len(stack) >1:
                stack[-1]=stack[-1]*2
                stack[-2]=stack[-2]*2
        elif i == "#":
            stack[-1] = stack[-1]*-1
        else:
            check_int+=i
    
    answer= sum(stack)
    return answer