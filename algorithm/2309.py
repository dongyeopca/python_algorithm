import itertools
a = list()
for i in range(9):
    a.append(int(input()))

combi = list(itertools.combinations(a,7))
for i in range(len(combi)):
    if sum(combi[i])==100:
        answer = sorted(list(combi[i]))
        break
for i in answer:
    print(i)


