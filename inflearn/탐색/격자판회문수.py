matrix = list()
cnt = 0
for i in range(7):
    a = list(map(int,input().split()))
    matrix.append(a)
    #가로체크
for k in range(7):
    for i in range(3):
        x = matrix[k][i:i+5]
        if x == x[::-1]:
            cnt+=1
            #세로체크
        for j in range(2):
            if matrix[i+j][k] != matrix[i+4-j][k]:
                break
        else:
            cnt+=1


