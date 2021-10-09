while True:
    w,h = map(int,input())
    if w == 0 and h==0:
        break
    else:
        matrix = []
        dx = [1,-1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
        for i in range(h):
            matrix.append(i)
        for i in range(dx)
