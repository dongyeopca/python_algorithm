n = int(input())
m = int(input())
channel = 100
remote = list()
live_button = {str(i) for i in range(10)}
if m>0:
    live_button-=set(map(str,input().split()))
min_cnt = abs(n-channel)
for i in range(100000):
    for j in range(len(str(i))):
        if str(i)[j] not in live_button:
            break
        elif len(str(i))-1==j:
            min_cnt = min(min_cnt,abs(i-n)+len(str(i)))

print(min_cnt)

