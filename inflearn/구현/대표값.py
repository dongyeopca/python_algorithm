# n = int(input())
# score = list(map(int,input().split()))
# s_score = sorted(score,reverse=True)
# average =round(sum(score)/n)
# answer = s_score[0]
# for i in range(1,n):
#     if abs(average-answer)>abs(average-s_score[i]):
#         answer = s_score[i]
# print(average,score.index(answer)+1)


n = int(input())
score = list(map(int,input().split()))
ave = round(sum(score)/n)#round는 round_half_even방식 채택 따라서 오류가 발생함 그러므로 0.5를 더하고 int()정수형 변환을 사용하자
min = 214700000
for idx,x in enumerate(score):
    tmp = abs(ave-x)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1
    elif tmp==min:
        if x>score:
            score = x
            res = idx+1