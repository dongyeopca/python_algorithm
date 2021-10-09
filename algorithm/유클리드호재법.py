def Gcd(a,b):
    while a%b!=0:
        a,b = b,a%b
    return b
def Lcm(a,b):
    return a*b//Gcd(a,b)

#여러 수의 최대공약수
arr = list(map(int,input().split()))
Gcdarr = arr[0]
Lcmarr = arr[0]
for i in range(1,len(arr)):
    Gcdarr = Gcd(Gcdarr,arr[i])
print(Gcdarr)
#여러수의 최소공배수
for i in range(1,len(arr)):
    Lcmarr = Lcm(Lcmarr,arr[i])
print(Lcmarr)

