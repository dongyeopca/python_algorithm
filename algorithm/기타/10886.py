n = int(input())
count =0
for i in range(n):
    choose = int(input())
    if choose == 0:
        count -=1
    else:
        count +=1
if count>0:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')