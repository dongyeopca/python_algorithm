a = list(map(int,input().split()))
b = max(a)
a.remove(b)
print(max(a))