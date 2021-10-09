import itertools
p = list()
for i in range(9):
    p.append(int(input()))

com = list(itertools.combinations(p,7))
for i in range(len(com)):
    if sum(com[i])==100:
        a=sorted(com[i])
        print(a)
        break

for i in range(n):