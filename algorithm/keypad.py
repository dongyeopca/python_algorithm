# def solution(numbers, hand):
#     answer = ''
#     L = 10
#     R = 12
#     for i in numbers:
#         if i in [1,4,7]:
#             answer += 'L'
#             L = i
#         elif i in [3,6,9]:
#             answer += 'R'
#             R = i
#         else:
#             if i==0: i=11
#             absL = abs(i-L)//3+abs(i-L)%3
#             absR = abs(i-R)//3+abs(i-R)%3
#             if absL<absR:
#                 answer +='L'
#                 L = i
#             elif absL>absR:
#                 answer +='R'
#                 R = i
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     L = i
#                 else:
#                     answer +='R'
#                     R = i
#     return answer
## 2차 푼거
def solution(numbers, hand):
    phone = [[1,4,7,"*"],[2,5,8,0],[3,6,9,"#"]]
    answer = ""
    left = ["*"]
    right = ["#"]
    for i in numbers:
        if i in phone[0]:
            answer += 'L'
            left.append(i)
            continue
        elif i in phone[2]:
            answer += "R"
            right.append(i)
            continue
        elif i in phone[1]:
            check = phone[1].index(i)
            if left[-1] in phone[1]:
                left_c = abs(phone[1].index(left[-1])-check)
            elif left[-1] in phone[0]:
                left_c = abs(phone[0].index(left[-1])-check)+1
            if right[-1] in phone[1]:
                right_c = abs(phone[1].index(right[-1])-check)
            elif right[-1] in phone[2]:
                right_c = abs(phone[2].index(right[-1])-check)+1
            if left_c == right_c:
                if hand == "right":
                    answer +='R'
                    right.append(i)
                elif hand == "left":
                    answer +="L"
                    left.append(i)
            elif right_c>left_c:
                answer+="L"
                left.append(i)
            elif left_c>right_c:
                answer +="R"
                right.append(i)
    print(answer)
                
                    