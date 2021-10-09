t = int(input())
for _ in range(t):
    n,s,e,k = map(int,input().split())
    array = list(map(int,input().split()))[s-1:e]
    a = sorted(array)
    print(_+1,a[k-1])

    
