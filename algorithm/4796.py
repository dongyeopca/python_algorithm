case = 1
while True:#l,p,v순으로 입력 연속되는 l일중 p일만 사용가능 v는 휴가일수
    a = list(map(int,input().split()))
    if a == [0,0,0]:
        break
    answer = (a[2]//a[1])*a[0] + min(a[2]%a[1],a[0])
    print(f'Case {case}: {answer}')
    case+=1
