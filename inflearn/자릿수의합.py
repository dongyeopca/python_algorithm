# n = int(input())
# a = list(map(int,input().split()))
# res = list()
# s = 0
# for i in a:
#     for j in str(i):
#         s+=int(j)
#     res.append(s)
#     s = 0
# print(a[res.index(max(res))])

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x =x//10
    return sum
