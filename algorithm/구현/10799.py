# import sys
# input = sys.stdin.readline()
# s = input
# count=list()
# answer =0
# stack = list()
# for i in s:
#     if stack:
#         if stack[-1]=="(" and i==")":
#             count.pop()
#             stack.append(i)
#             for k in range(len(count)):
#                 count[k]+=1
#         elif stack[-1] == ")" and i==")":
#             stack.append(i)
#             answer +=count[-1]
#             count.pop()
#         else:
#             stack.append(i)
#             count.append(1)
#     else:
#         stack.append(i)
#         count.append(1)

a = list(input())
s = []
b = 0

for i in range(len(a)):
    if a[i] == "(":
        s.append("(")
    else:#")"
        if a[i-1] == "(":
            s.pop()
            b=b+len(s)
            #((()))
        else:#")"
            s.pop()
            b=b+1
print(b)


# print(answer)
#시작점과 끝점 체크/그 사이 레이저 체크
#레이저의 갯수 체크
#막대기가 열리고 닫히기까지 레이져의 갯수+1=>쪼개진갯수
