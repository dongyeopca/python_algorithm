# def solution(number,k):
#     answer = ""
#     stack = []

#     for index,num in enumerate(number):
#         while len(stack)>0 and k>0 and stack[-1]<num:
#             stack.pop()
#             k -=1
#         if k==0:
#             stack+=number[index:]
#             break
#         stack.append(num)
#     if k>0:
#         stack = stack[:len(number)-k]
#     answer = ''.join(stack)
#     print(answer)
# solution("4177252841",4)
print("10+8-10".split('-'))
