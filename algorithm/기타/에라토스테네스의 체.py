#n이하의 모든 소수를 구하기
n = int(input())#입력
a = [True]*n
m = int(n**0.5)

for i in range(2,m+1):
    if a[i] ==True:
        for j in range(2*i,n,i):
            a[j]=False

print([i for i in range(2,n) if a[i] ==True])

print(reversed(sorted('hello')))