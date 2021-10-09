n = int(input())
correct = list(map(int,input().split()))
score = 0
stack = list()
for i in correct:
    if i == 1:
        stack.append(i)
        score+=len(stack)
    else:
        stack = list()
print(score)