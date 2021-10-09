# score = input()
# answer = 0
# if score[0]=='A':
#     answer+=4
# elif score[0]=='B':
#     answer +=3
# elif score[0]=="C":
#     answer +=2
# elif score[0]=="D":
#     answer +=1
# else:
#     answer = 0
# if score[1]=="+":
#     answer +=0.3
# elif score[1]=="-":
#     answer -= 0.3
# else:
#     answer += 0
# print(float(answer))

grade = {
    'A+': 4.3,'A0':4.0,'A-':3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}
print(grade[input()])