while True:
    first,second = list(map(int,input().split()))
    if first == 0 and first==second:
        break
    if second%first==0:
        print("factor")
    elif first%second==0:
        print("multiple")
    else:
        print('neither')
