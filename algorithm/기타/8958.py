n = int(input())
for i in range(n):
    quiz = input()
    count= list()
    score = 0
    for j in quiz:
        if j == "O":
            if count:
                if count[-1]==j:
                    count.append(j)
                    score+=len(count)
            else:
                count.append(j)
                score+=1
        else:
            count = list()
    print(score)
