from sys import stdin

stack1 = list(stdin.readline().strip())
n = int(input())#입력할 명령어의 수
stack2 = list()

for i in range(n):
    order = stdin.readline()
    if order[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif order[0] == "D":
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif order[0] == "B":
        if stack1:
            stack1.pop()
        else:
            continue
    elif order[0] == "P":
        stack1.append(order[2])

stack1.extend(stack2[::-1])
print(''.join(stack1))