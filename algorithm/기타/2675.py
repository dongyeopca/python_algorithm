n = int(input())
for i in range(n):
    answer = ""
    s = input().split()
    a =int(s[0])
    for j in range(len(s[1])):
        answer +=s[1][j]*a
    print(answer)
    