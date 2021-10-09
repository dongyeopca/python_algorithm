time = int(input())
button = 0
a =300
b =60
c =10
buttona = 0
buttonb = 0
buttonc = 0
while time>0:
    if time>=a:
        time-=a
        buttona+=1
    elif time<a and time>=b:
        time-=b
        buttonb+=1
    elif time<b:
        time-=c
        buttonc+=1
if time<0:
    print(-1)
else:
    print(buttona,buttonb,buttonc)
