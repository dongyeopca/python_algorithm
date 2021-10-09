n= int(input())
for i in range(n):
    a = input().split()
    answer = float(a[0])
    for j in a:
        if j == "@":
            answer =answer*3
        if j == "#":
            answer -= 7
        if j == "%":
            answer +=5
    
    print("%0.2f"%answer)#소수점 2째자리까지만 출력.
