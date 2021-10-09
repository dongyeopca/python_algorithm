def solution():
    toggle = True
    while toggle:
        a,b = map(int,input().split())
        if a==b and a==0:
            toggle = False
            break
        if a>b:
            print('Yes')
        else:
            print('No')
        

solution()