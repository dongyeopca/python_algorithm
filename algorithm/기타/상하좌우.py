n = map(int,input())
list = map(str,input().split())
x,y = 1,1
for i in list:
    if i == 'L':
        if y ==1:
            pass
        else:y -=1
        
    elif i == 'R':
        y+=1
    elif i == 'U':
        if x==1:
            pass
        else:
            x-=1
    elif i == 'D':
        x+=1

print(x,y)
