n = int(input())
q1=0
q2=0
q3=0
q4=0
axis=0
for i in range(n):
    x,y = list(map(int,input().split()))
    if x>0 and y>0:
        q1+=1
    elif x<0 and y>0:
        q2+=1
    elif x<0 and y<0:
        q3+=1
    elif x>0 and y<0:
        q4+=1
    elif x==0 or y==0:
        axis+=1

print("Q1:",q1,"\nQ2:",q2,"\nQ3:",q3,"\nQ4:",q4,"\nAXIS:",axis)
