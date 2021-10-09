n = int(input())
for i in range(n):
    Yonsei=0
    Korea=0
    for i in range(9):
        a,b = list(map(int,input().split()))
        Yonsei+=a
        Korea+=b
    if Yonsei>Korea:
        print('Yonsei')
    elif Yonsei<Korea:
        print('Korea')
    else:
        print('Draw')

