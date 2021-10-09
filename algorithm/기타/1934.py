
#최소공배수 문제
n = int(input())
for i in range(n):
    a,b = list(map(int,input().split()))
    #최대 공약수(유클리드 호제법)
    def gcd(a,b):
        while b>0:
            a,b=b,a%b
        return a
    print(int(a*b/gcd(a,b)))
