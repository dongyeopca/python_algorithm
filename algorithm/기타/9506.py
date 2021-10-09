num = int(input())
while True:
    if num == -1:break
    locker = list()
    for i in range(1,int(num/2)+1):
        if num%i==0:
            locker.append(i)
    if sum(locker) == num:
        print(f'{num} = {locker[0]}',end='')
        for i in range(1,len(locker)):
            print(f' + {locker[i]}',end="")
        print()
    else:
        print(f'{num} is NOT perfect.')
    num = int(input())
    

    #그냥 txt변수 만들어서 거기에 더해주면됨..병신같이 풀었네..