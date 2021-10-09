import itertools
a = 'ABC'
print(list(map(''.join,itertools.permutations(a))))#순열
print(list(map("".join,itertools.combinations(a,2))))