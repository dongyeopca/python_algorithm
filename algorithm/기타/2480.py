number = list(map(int,input().split()))
count_list = list()
for i in number:
   count_list.append(number.count(i))
answer = max(count_list)
if answer == 3:
    print(10000+number[0]*1000)
elif answer == 2:
    print(1000+number[count_list.index(2)]*100)
elif answer == 1:
    print(max(number)*100)
