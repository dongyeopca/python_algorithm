# #재귀
# def fibo(x):
#     if x ==0:
#         return 0
#     elif x==1:
#         return 1
#     else:
#         return fibo(x-1)+fibo(x-2)

# print(fibo(6))
# #반복문
# def fibo(x):
#     current,next = 0,1
#     for _ in range(x):
#         current,next = next,current+next
#     return current
# print(fibo(100))

t = int(input())

def fibo(x):
    if x ==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

for _ in range(t):
    fibo_ = list()
    want = int(input())
    answer = list()
    i=1
    while True:
        if fibo(i)>want:
            break
        else:
            fibo_.append(fibo(i))
            i+=1
    for i in range(len(fibo_)-1,-1,-1):
        print(answer)
        if fibo_[i]<=want:
            answer.append(fibo_[i])
            want-=fibo_[i]
        else:
            pass
        if want==0:
            answer.sort()
            for i in answer:
                print(i,end=' ')
            break
#시간초과
#dp 개념 적용해야할듯
