a = input()
count = 0
stack = list()
for i in a:
    if stack:
        if i == stack[-1]:
            count+=5
            stack.append(i)
        else:
            count+=10
            stack.append(i)
    else:
        count+=10   
        stack.append(i)    
print(count)