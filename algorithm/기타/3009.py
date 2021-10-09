x_list = list()
y_list = list()
answer = [[],[]]
for i in range(3):
    x,y= list(map(int,input().split()))
    x_list.append(x)
    y_list.append(y)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        answer[0].append(x_list[i])
    if y_list.count(y_list[i]) == 1:
        answer[1].append(y_list[i])

print(answer[0][0],answer[1][0])