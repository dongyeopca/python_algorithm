s = input()
cnt = 0
answer = ''
for i in s:
    if i.isdecimal():
        answer+=i
print(int(answer))
for i in range(1,int(answer)+1):
    if int(answer)%i==0:
            cnt+=1
print(cnt)